VERSION = (0, 1)

API_URL = 'https://api.zenmoney.ru'
URI_AUTH = API_URL + '/oauth2/authorize/'
URI_TOKEN = API_URL + '/oauth2/token/'
URI_REDIRECT = 'notscheme://localhost/'
URI_DIFF = API_URL + '/v8/diff/'
URI_SUGGEST = API_URL + '/v8/suggest/'
OBJECT_CLASS_NAME_LIST = (
    'account',
    'budget',
    'company',
    'instrument',
    'merchant',
    'reminder',
    'reminderMarker',
    'tag',
    'transaction',
    'user',
)
