import requests
import json


baseUrl = f"https://itunes.apple.com/search?"
r = requests.get(baseUrl, params={'term': 'the beatles', 'country': 'us','limit': 3})
# print(r.status_code)
# print(r.url)
info = r.json()
# print(info.keys())
print(len(info['results']))
print(json.dumps(info['results'], indent=4, sort_keys=True))




