import requests
import json

date = input('Please enter "latest" or a date in YYYY-MM-DD format: ')
base = input('Convert from (currency - EUR is the only available free option):) ')
curr = input('Convert to (currency): ')
quan = float(input('How much {} do you want to convert? '.format(base)))

accessKey = 'b5af89a7098ae2d487a95f40fb24007e'  
baseUrl = f'http://api.exchangeratesapi.io/v1/'
url  = f'{baseUrl}{date}?access_key={accessKey}&base={base}&symbols={curr}'
response = requests.get(url)
data = response.json()
# print(response.status_code)
# print(data)
# print(json.dumps(data, indent=4, sort_keys=True))

if response.status_code != 200:
    print('Sorry, there was a problem retrieving the data. Please try again.')
    print(response.json()['error']) 

else:
    rate = data['rates'][curr]
    result = (quan * rate)
    print(f'{"%.2f" % quan} {base} is equal to {"%.2f" % result} {curr}, based on exchange rates for {data["date"]}.')    
