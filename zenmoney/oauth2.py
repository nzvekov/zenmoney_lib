import time
from dataclasses import dataclass
from http import HTTPStatus
from typing import Optional

import requests

from zenmoney.base import BaseZenmoneyRequest
from zenmoney.constant import API_URL
from zenmoney.exception import ZenmoneyError

URI_AUTH = API_URL + '/oauth2/authorize/'
URI_TOKEN = API_URL + '/oauth2/token/'
URI_REDIRECT = 'notscheme://localhost/'


@dataclass
class Token:
    access_token: str
    token_type: str
    expires_in: int
    refresh_token: str

    @property
    def is_valid(self) -> bool:
        return int(time.time()) < self.expires_in


class OAuth2ZenmoneyClient(BaseZenmoneyRequest):
    def __init__(self, consumer_key: str, consumer_secret: str, username: str, password: str):
        super().__init__()
        self.consumer_key = consumer_key
        self.consumer_secret = consumer_secret
        self.username = username
        self.password = password
        self._token: Optional[Token] = None

    @property
    def token(self):
        if self._token is None or not self._token.is_valid:
            self._token = self.get_token()
        return self._token

    def get_token(self):
        code = self.get_code()
        response = self.post(
            URI_TOKEN,
            data={
                'grant_type': 'authorization_code',
                'client_id': self.consumer_key,
                'client_secret': self.consumer_secret,
                'code': code,
                'redirect_uri': URI_REDIRECT,
            },
        )
        if response.status_code != HTTPStatus.OK:
            raise ZenmoneyError(f"Failed to get token: {response.text}")

        return Token(**response.json())

    def get_code(self) -> str:
        self.session.get(
            URI_AUTH,
            params={
                'response_type': 'code',
                'client_id': self.consumer_key,
                'redirect_uri': URI_REDIRECT,
            },
        )
        response = self.post(
            URI_AUTH,
            json={
                'username': self.username,
                'password': self.password,
                'auth_type_password': 'Sign in',
            },
            allow_redirects=False,
        )
        if response.status_code != HTTPStatus.FOUND:
            raise ZenmoneyError("Authorization failed")

        code_redirect = response._next.url
        code_query = requests.utils.urlparse(code_redirect).query
        code_dict = dict(x.split('=') for x in code_query.split('&'))
        if not code_dict.get('code', False):
            raise ZenmoneyError(
                "User authorization redirect url {} does not contain 'code' parameter".format(code_redirect),
            )
        return code_dict.get('code')
