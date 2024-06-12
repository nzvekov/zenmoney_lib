## Python library for ZenMoney API
This library allows you to use [ZenMoney API](https://github.com/zenmoney/ZenPlugins/wiki/ZenMoney-API).

There is a simplest way to start:

```python
import time

from zenmoney import Diff, ZenmoneyOAuth2, ZenmoneyRequest

oauth = ZenmoneyOAuth2('your_consumer_key', 'your_consumer_secret', 'user_name', 'user_password')
zenmoney_client = ZenmoneyRequest(oauth.token.access_token)
server_timestamp = 0
current_timestamp = int(time.time())
params = Diff(
    server_timestamp=server_timestamp,
    current_client_timestamp=current_timestamp,
)
data = zenmoney_client.diff(params=params)
```
