import requests
import json

baseUrl = "http://api.exchangeratesapi.io/v1/latest?access_key=b5af89a7098ae2d487a95f40fb24007e"
paramURL = baseUrl + "&symbols=USD,GBP"
response = requests.get(paramURL)

print(response.status_code)
# print(json.dumps(response.json(), indent=4, sort_keys=True))
# print(response.json().keys())
# print(paramURL)

data = response.json()

print(f'here is the base = {data["base"]}')
print(f'here is the base = {data["date"]}')
print(f'here is the base = {data["rates"]}')