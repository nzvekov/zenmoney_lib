"""Check the library against the live API with an OAuth access token.

    uv run python scripts/check_live_api.py [FIXTURE_PATH]

Reads ZENMONEY_TOKEN and ZENMONEY_TOKEN_RECEIVED_AT (unix time) from `.env.spike`
(git-ignored, like every `.env.*`). Three checks:

A. the full diff (serverTimestamp=0) parses into `Diff`; with FIXTURE_PATH an
   anonymized copy of the raw response is written there;
B. a light diff (serverTimestamp=now, forceFetch=["user"]) lists the same users;
C. the token still works, and how old it is (re-run after 25–48 h).
"""

import asyncio
import json
import os
import sys
import time
from collections import Counter

from dotenv import load_dotenv
from pydantic import ValidationError

from zenmoney import AsyncZenmoneyRequest
from zenmoney.exception import ZenmoneyRequestError
from zenmoney.models import Diff

load_dotenv(".env.spike")

# Free text that may identify the person; amounts, dates and ids stay so the data keeps its shape.
_TEXT_FIELDS = {
    "account": ("title",),
    "merchant": ("title",),
    "tag": ("title",),
    "transaction": ("payee", "originalPayee", "comment", "qrCode", "incomeBankID", "outcomeBankID"),
    "reminder": ("payee", "comment"),
    "reminderMarker": ("payee", "comment"),
}
_DROP_FIELDS = {
    "account": ("syncID",),
    "transaction": ("latitude", "longitude"),
    "user": ("email", "login"),
}
# Fixture size caps: the parse checks need every shape, not the whole history.
_MAX_TRANSACTIONS = 500
_MAX_MARKERS = 300
_BUDGET_MONTHS = 3


def anonymize(raw: dict) -> dict:
    out = json.loads(json.dumps(raw))
    for entity, fields in _TEXT_FIELDS.items():
        for n, row in enumerate(out.get(entity) or [], 1):
            for f in fields:
                if row.get(f):
                    row[f] = f"{entity} {f} {n}"
    for entity, fields in _DROP_FIELDS.items():
        for row in out.get(entity) or []:
            for f in fields:
                if f in row:
                    row[f] = None if f != "email" else f"user{row.get('id')}@example.com"
    txs = sorted(out.get("transaction") or [], key=lambda t: t.get("date") or "", reverse=True)
    out["transaction"] = txs[:_MAX_TRANSACTIONS]
    markers = sorted(out.get("reminderMarker") or [], key=lambda m: m.get("date") or "", reverse=True)
    out["reminderMarker"] = markers[:_MAX_MARKERS]
    months = sorted({b["date"] for b in out.get("budget") or []}, reverse=True)[:_BUDGET_MONTHS]
    out["budget"] = [b for b in out.get("budget") or [] if b["date"] in months]
    # Keep only directory rows the remaining data points at.
    used = {a.get("company") for a in out.get("account") or []}
    out["company"] = [c for c in out.get("company") or [] if c["id"] in used]
    used = {r.get("merchant") for k in ("transaction", "reminder", "reminderMarker") for r in out.get(k) or []}
    out["merchant"] = [m for m in out.get("merchant") or [] if m["id"] in used]
    return out


def parse_report(raw: dict) -> list[str]:
    """Every validation error, by entity, so one bad row does not hide the rest."""
    try:
        Diff.from_dict(raw)
        return []
    except ValidationError as err:
        return [f"{'.'.join(map(str, e['loc']))}: {e['msg']} (got {e.get('input')!r:.80})" for e in err.errors()]


async def main() -> int:
    token = os.environ["ZENMONEY_TOKEN"]
    received_at = int(os.getenv("ZENMONEY_TOKEN_RECEIVED_AT", "0"))
    fixture = sys.argv[1] if len(sys.argv) > 1 else None
    now = int(time.time())

    async with AsyncZenmoneyRequest(token, timeout=(10.0, 300.0)) as client:
        # C first: a dead token makes A and B meaningless.
        try:
            await client.raw_diff(Diff(server_timestamp=now, current_client_timestamp=now).to_dict())
            age = f"{(now - received_at) / 3600:.1f} h" if received_at else "unknown age"
            print(f"C. token works ({age})")
        except ZenmoneyRequestError as err:
            print(f"C. token rejected: {err}")
            return 1

        started = time.monotonic()
        raw = await client.raw_diff(Diff(server_timestamp=0, current_client_timestamp=now).to_dict())
        took = time.monotonic() - started
        sizes = Counter({k: len(v) for k, v in raw.items() if isinstance(v, list)})
        print(f"A. full diff in {took:.1f} s, {len(json.dumps(raw)) / 1e6:.1f} MB: {dict(sizes)}")
        errors = parse_report(raw)
        print("A. parses into Diff" if not errors else f"A. {len(errors)} validation errors:")
        for line in errors[:40]:
            print("   ", line)
        intervals = Counter(r.get("interval") for r in raw.get("reminder") or [])
        types = Counter(a.get("type") for a in raw.get("account") or [])
        print(f"   reminder intervals: {dict(intervals)}; account types: {dict(types)}")
        print(f"   users: {[(u['id'], u.get('parent')) for u in raw.get('user') or []]}")
        if fixture:
            with open(fixture, "w", encoding="utf-8") as f:
                json.dump(anonymize(raw), f, ensure_ascii=False, indent=1)
            print(f"   fixture written: {fixture}")

        started = time.monotonic()
        light = await client.raw_diff(
            Diff(server_timestamp=now, current_client_timestamp=now, force_fetch=["user"]).to_dict()
        )
        took = time.monotonic() - started
        full_users = sorted(u["id"] for u in raw.get("user") or [])
        light_users = sorted(u["id"] for u in light.get("user") or [])
        verdict = "same users" if light_users == full_users else f"DIFFERENT: {light_users} vs {full_users}"
        print(f"B. forceFetch=['user'] in {took:.1f} s: {verdict}")
    return 0 if not errors else 2


if __name__ == "__main__":
    sys.exit(asyncio.run(main()))
