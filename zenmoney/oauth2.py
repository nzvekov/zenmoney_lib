from http import HTTPStatus
from typing import Optional
from urllib.parse import urlparse

from .base import BaseZenmoneyRequest
from .constant import AUTH_URL, DEFAULT_TIMEOUT, REDIRECT_URL, TOKEN_URL
from .exception import ZenmoneyRequestError
from .models import Token
from .utils import convert_response_to_json


class ZenmoneyOAuth2(BaseZenmoneyRequest):
    def __init__(
        self,
        consumer_key: str,
        consumer_secret: str,
        username: str,
        password: str,
        *,
        timeout: float | tuple[float, float] | tuple[float, None] | None = DEFAULT_TIMEOUT,
        token_url: str = TOKEN_URL,
        auth_url: str = AUTH_URL,
        redirect_url: str = REDIRECT_URL,
    ):
        super().__init__(timeout=timeout)
        self.consumer_key = consumer_key
        self.consumer_secret = consumer_secret
        self.username = username
        self.password = password
        self._token: Optional[Token] = None
        self._token_url = token_url
        self._auth_url = auth_url
        self._redirect_url = redirect_url

    @property
    def token(self) -> Token:
        if self._token is None or not self._token.is_valid:
            self._token = self._get_token()
        return self._token

    def _get_token(self) -> Token:
        code = self._get_code()
        response = self._post(
            self._token_url,
            data={
                'grant_type': 'authorization_code',
                'client_id': self.consumer_key,
                'client_secret': self.consumer_secret,
                'code': code,
                'redirect_uri': REDIRECT_URL,
            },
        )
        if response.status_code != HTTPStatus.OK:
            raise ZenmoneyRequestError(f"Failed to get token: {response.text}")

        return Token(**convert_response_to_json(response))

    def _get_code(self) -> str:
        self._get(
            self._auth_url,
            params={
                'response_type': 'code',
                'client_id': self.consumer_key,
                'redirect_uri': REDIRECT_URL,
            },
        )
        response = self._post(
            self._auth_url,
            json={
                'username': self.username,
                'password': self.password,
                'auth_type_password': 'Sign in',
            },
            allow_redirects=False,
        )
        if response.status_code != HTTPStatus.FOUND:
            raise ZenmoneyRequestError("Authorization failed")
        code_redirect = response.next.url
        code_query = urlparse(code_redirect).query
        code_dict = dict(x.split('=') for x in code_query.split('&'))
        if not code_dict.get('code', False):
            raise ZenmoneyRequestError(
                f"User authorization redirect url {code_redirect} does not contain 'code' parameter",
            )
        return code_dict.get('code')
