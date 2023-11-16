import requests
import json


baseSite = f'https://jobs.github.com/positions.json'
# r = requests.get(baseSite, params={'description': 'data science', 'location': 'san francisco'})
r = requests.get(baseSite)
print(r.status_code)
print(r.ok)
# print(json.dumps(r.json(), indent=4))
# this part of the course needs some updating