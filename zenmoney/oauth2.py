import time
from dataclasses import dataclass
from http import HTTPStatus
from typing import Optional
from urllib.parse import urlparse

from .base import BaseZenmoneyRequest
from .constant import URI_AUTH, URI_REDIRECT, URI_TOKEN
from .exception import ZenmoneyError
from .utils import convert_response_to_json


@dataclass
class Token:
    access_token: str
    token_type: str
    expires_in: int
    refresh_token: str

    @property
    def is_valid(self) -> bool:
        return int(time.time()) < self.expires_in


class ZenmoneyOAuth2(BaseZenmoneyRequest):
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

        return Token(**convert_response_to_json(response))

    def get_code(self) -> str:
        self.get(
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
        code_query = urlparse(code_redirect).query
        code_dict = dict(x.split('=') for x in code_query.split('&'))
        if not code_dict.get('code', False):
            raise ZenmoneyError(
                f"User authorization redirect url {code_redirect} does not contain 'code' parameter",
            )
        return code_dict.get('code')
