import requests
import json

baseUrl = "http://api.exchangeratesapi.io/v1/latest?access_key=b5af89a7098ae2d487a95f40fb24007e"

response = requests.get(baseUrl)

print(response.status_code)
print(response.json())