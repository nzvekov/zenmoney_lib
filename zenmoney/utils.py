from datetime import datetime

from requests import JSONDecodeError, Response

from .exception import ZenmoneyRequestError


def timestamp(date: datetime = None) -> int:
    if date:
        return int(datetime.timestamp(date))

    return int(datetime.timestamp(datetime.now()))


def convert_response_to_json(response: Response) -> dict:
    try:
        return response.json()
    except JSONDecodeError as err:
        raise ZenmoneyRequestError('Failed to convert response to JSON', err) from err
