import requests
import random

def random_city_name():
    city_name = []
    for i in range(1000):
        city_name.append(random.choice(requests.get('https://gist.githubusercontent.com/Miserlou/c5cd8364bf9b2420bb29/raw/2bf258763cdddd704f8ffd3ea9a3e81d25e2c6f6/cities.json').json()))
    return city_name

random_city_name()

for i in random_city_name():
    if len(i['city']) == 3:
        print(i['city'])