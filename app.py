import requests
import json

baseUrl = "http://api.exchangeratesapi.io/v1/latest?access_key=b5af89a7098ae2d487a95f40fb24007e"
paramURL = baseUrl + "&symbols=GBP" + "&" + "base=EUR"  #had to use EUR as base as all other currencies are only available for paid subscription
data = requests.get(paramURL).json()

eurToGbp = data["rates"]["GBP"]
print(f'1 GBP in EUR = {eurToGbp}')



# print(json.dumps(response.json(), indent=4, sort_keys=True))
# print(response.json().keys())
# print(paramURL)

# print(f'here is the base = {data["base"]}')
# print(f'here is the base = {data["date"]}')
# print(f'here is the base = {data["rates"]}')