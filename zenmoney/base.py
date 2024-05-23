import requests

from .exception import ZenmoneyError


class BaseZenmoneyRequest(object):
    def __init__(self):
        self.session = requests.Session()

    def post(self, uri: str, **kwargs):
        response = self.session.post(uri, **kwargs)
        if not response.ok:
            raise ZenmoneyError(
                'POST request to {} wasn\'t successful, code={}'.format(uri, response.status_code),
                uri=uri,
                response=response,
            )
        return response
