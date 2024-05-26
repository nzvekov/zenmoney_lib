from datetime import datetime

import requests


def timestamp(date: datetime = None) -> int:
    if date:
        return int(datetime.timestamp(date))

    return int(datetime.timestamp(datetime.now()))


def convert_response_to_json(response: requests.Response) -> dict:
    try:
        return response.json()
    except ValueError as error:
        raise ValueError('Failed to convert response to JSON', error)
