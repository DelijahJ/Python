from urllib.request import urlopen
import json
import csv
import pprint

api_url = 'https://acnhapi.com/v1/'

api_request = urlopen(api_url + 'fish')

api_request = api_request.read()

data = json.loads(api_request)

with open('fish_data.json', 'w') as f:
    writer = csv.writer(f)

    headers = ['Name', 'ID', 'Rarity']
    
    writer.writerow(headers)

    for bug in data:
        b = [
            data[bug]['name']['name-USen'],
            data[bug]['id'],
            data[bug]['availability']['rarity']
        ]
        writer.writerow(b)
    #json.dump(data, f, indent=2)