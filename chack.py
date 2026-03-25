import pprint
import time
from zenmoney import ZenmoneyOAuth2, ZenmoneyRequest
from zenmoney.models import Diff

oauth = ZenmoneyOAuth2(
    consumer_key='gdd0914d51e331ffa03ac97d947582',
    consumer_secret='f3f0c564d1',
    username='hassler494',
    password='Cnhtktw30!'
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
