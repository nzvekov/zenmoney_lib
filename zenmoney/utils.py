from datetime import datetime

from exception import ZenmoneyRequestError
from requests import JSONDecodeError, Response


def timestamp(date: datetime = None) -> int:
    if date:
        return int(datetime.timestamp(date))

    return int(datetime.timestamp(datetime.now()))


def convert_response_to_json(response: Response) -> dict:
    try:
        return response.json()
    except JSONDecodeError as err:
        raise ZenmoneyRequestError('Failed to convert response to JSON', err) from err
