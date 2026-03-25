# ZenMoney Python Library

A Python library for interacting with the [ZenMoney API](https://github.com/zenmoney/ZenPlugins/wiki/ZenMoney-API). This library provides a simple and intuitive interface to work with ZenMoney's financial management platform.

## Features

- OAuth2 authentication
- Synchronization with ZenMoney server
- Support for all ZenMoney API endpoints
- Type-safe models for request/response data
- Error handling and exception management

## Installation

You can install the library using pip:

```bash
pip install zenmoney-py
```

## Requirements

- Python 3.10 or higher
- requests >= 2.32.3

## Quick Start

Here's a simple example of how to use the library:

```python
import time
from zenmoney import ZenmoneyOAuth2, ZenmoneyRequest
from zenmoney.models import Diff

# Initialize OAuth2 client
oauth = ZenmoneyOAuth2(
    consumer_key='your_consumer_key',
    consumer_secret='your_consumer_secret',
    username='your_username',
    password='your_password'
)

# Create API client
zenmoney_client = ZenmoneyRequest(oauth.token.access_token)

# Prepare synchronization parameters
server_timestamp = 0
current_timestamp = int(time.time())
params = Diff(
    server_timestamp=server_timestamp,
    current_client_timestamp=current_timestamp,
)

# Get data from ZenMoney
data = zenmoney_client.diff(params=params)
```

## Authentication

The library uses OAuth2 for authentication. You'll need to provide:
- Consumer Key
- Consumer Secret
- Username
- Password

These credentials can be obtained from your ZenMoney account settings.

## Available Endpoints

The library supports the two main ZenMoney API endpoints:

### Diff Endpoint
The `diff` endpoint is used for synchronization with the ZenMoney server. It allows you to:
- Get the latest changes from the server
- Send your local changes to the server
- Maintain data consistency between client and server

Example usage:
```python
# Get server changes
data = zenmoney_client.diff(params=Diff(
    server_timestamp=0,
    current_client_timestamp=int(time.time())
))
```

### Suggest Endpoint
The `suggest` endpoint helps with transaction categorization and payee suggestions. It can:
- Suggest categories for transactions
- Recommend payees based on transaction details
- Help with transaction tagging

Example usage:
```python
# Get suggestions for a transaction
suggestions = zenmoney_client.raw_suggest({
    "payee": "McDonalds"
})
```

## Development

To set up the development environment:

1. [Install uv](https://docs.astral.sh/uv/getting-started/installation/) if you haven't already.

2. Clone the repository:
```bash
git clone https://github.com/cooper30/zenmoney_lib.git
cd zenmoney_lib
```

3. Install dependencies and create virtual environment:
```bash
uv sync
```

4. Run tests:
```bash
uv run pytest
```

5. Lint and format code:
```bash
uv run ruff check .
uv run ruff format .
```

6. Install pre-commit hooks (optional, but recommended):
```bash
uv run pre-commit install
```
After that, ruff and pytest will run automatically on each commit.

## CI

GitHub Actions workflows:
- **codestyle** — ruff check + ruff format (on PR to develop/master)
- **test** — pytest on Python 3.10, 3.11, 3.12 (on PR and push to develop/master)

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Author

- Nikita Zvekov (hassler494@gmail.com)

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.
