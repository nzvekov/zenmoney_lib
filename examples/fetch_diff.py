"""Fetch the Zenmoney diff and pretty-print it.

Settings are read from environment variables or a `.env` file in the project root
(see `.env.template`).
"""

import os
import pprint
import time

from dotenv import load_dotenv

from zenmoney import ZenmoneyOAuth2, ZenmoneyRequest
from zenmoney.models import Diff

load_dotenv()

oauth = ZenmoneyOAuth2(
    consumer_key=os.environ["ZENMONEY_CONSUMER_KEY"],
    consumer_secret=os.environ["ZENMONEY_CONSUMER_SECRET"],
    username=os.environ["ZENMONEY_USERNAME"],
    password=os.environ["ZENMONEY_PASSWORD"],
)

zenmoney_client = ZenmoneyRequest(oauth.token.access_token)

server_timestamp = int(os.getenv("ZENMONEY_SERVER_TIMESTAMP", "0"))
current_timestamp = int(time.time())
params = Diff(
    server_timestamp=server_timestamp,
    current_client_timestamp=current_timestamp,
)

data = zenmoney_client.diff(params=params)

pprint.pprint(data.to_dict(), indent=4)
