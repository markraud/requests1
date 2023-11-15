import requests
import json

# histDate = '/2016-01-26'

accessKey = 'b5af89a7098ae2d487a95f40fb24007e'
baseUrl = f"http://api.exchangeratesapi.io/v1/"
# paramURL = f"{baseUrl}{dateVal}?access_key={accessKey}"
timePeriod = f"{baseUrl}timeseries?access_key={accessKey}&start_date=2017-04-26&end_date=2018-04-26&base=EUR&symbols=GBP"
response = requests.get(timePeriod)
data = response.json()
print(response.status_code)
print(json.dumps(data, indent=4, sort_keys=True))


# eurToGbp = data["rates"]["GBP"]
# print(f'1 GBP in EUR = {eurToGbp}')