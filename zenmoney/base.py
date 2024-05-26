import requests

from .exception import ZenmoneyError
from .utils import convert_response_to_json


class BaseZenmoneyRequest(object):
    def __init__(self):
        self.session = requests.Session()

    def get(self, uri: str, **kwargs):
        response = self.session.get(uri, **kwargs)
        if not response.ok:
            raise ZenmoneyError(
                f'GET request to {uri} wasn\'t successful, code={response.status_code}',
            )
        return response

    def post(self, uri: str, **kwargs):
        response = self.session.post(uri, **kwargs)
        if not response.ok:
            raise ZenmoneyError(
                f'POST request to {uri} wasn\'t successful, code={response.status_code}',
            )
        return response

    def post_and_parse_response_json(self, uri: str, data: dict) -> dict:
        response = self.post(uri, json=data)
        return convert_response_to_json(response)
