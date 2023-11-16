import requests
import json


baseUrl = f"https://itunes.apple.com/search"
r = requests.get(baseUrl, params={'term': 'the beatles', 'country': 'us','limit': 200})
# print(r.status_code)
print(r.url)
info = r.json()
# print(info.keys())
# print(len(info['results']))
print(json.dumps(info, indent=4))
# print(info['results'][0]['trackName'])




