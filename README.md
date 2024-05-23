## Python library for ZenMoney API
This library allows you to use [ZenMoney API](https://github.com/zenmoney/ZenPlugins/wiki/ZenMoney-API).

There is a simplest way to start:

```python
from zenmoney import *

oauth = OAuth2('consumer_key', 'consumer_secret', 'username', 'user_password')
api = ZenmoneyRequest(oauth.token.access_token)
params = Diff.from_dict(
    {
        'serverTimestamp': server_timestamp,
        'currentClientTimestamp': current_timestamp,
    }
)
data = zenmoney_client.diff(params=params)
```