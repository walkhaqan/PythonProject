import requests

import test_api

params = {"a": 1}
response =requests.get("https://www.baidu.com/", params=params)
print(response.text)
print(response.status_code)
print(response.url)
print(response.headers)
