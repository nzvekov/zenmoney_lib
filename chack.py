import pprint
import time
from zenmoney import ZenmoneyOAuth2, ZenmoneyRequest
from zenmoney.models import Diff

oauth = ZenmoneyOAuth2(
    consumer_key='***REMOVED***',
    consumer_secret='***REMOVED***',
    username='***REMOVED***',
    password='***REMOVED***'
)

zenmoney_client = ZenmoneyRequest(oauth.token.access_token)

server_timestamp = 0
current_timestamp = int(time.time())
params = Diff(
    server_timestamp=server_timestamp,
    current_client_timestamp=current_timestamp,
)

data = zenmoney_client.diff(params=params)

pprint.pprint(data.to_dict(), indent=4)
