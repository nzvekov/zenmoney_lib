from . import models as zenmodels  # noqa
from .oauth2 import ZenmoneyOAuth2  # noqa
from .request import ZenmoneyRequest  # noqa


def __getattr__(name):
    # Lazy: httpx is an optional extra, so sync users never import it.
    if name == "AsyncZenmoneyRequest":
        from .async_request import AsyncZenmoneyRequest

        return AsyncZenmoneyRequest
    raise AttributeError(f"module {__name__!r} has no attribute {name!r}")
