### <your text>
# Code:

### Write function on Python 3 that creates 1000 different random city names in list, getting cities name from internet.
# Code:

import random
import requests
import json

def get_city_name():
    url = 'https://randomuser.me/api/?results=1000'
    response = requests.get(url)
    data = json.loads(response.text)
    cities = []
    for i in range(1000):
        cities.append(data['results'][random.randint(0, len(data['results'])-1)]['location']['city'])
    return cities

print(get_city_name())