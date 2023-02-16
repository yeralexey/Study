"""
Interesting generations by https://t.me/CodefyBot after testedin main.py
"""

import json
import random
import requests



# repeat the fast Euclid algorithm for finding the greatest common divisor of two positive integers a and b.
# Named "get_nod" .
# Takes two arguments a and b (natural numbers) and returns the computed value greatest common devisor.

def get_nod(a, b):
    """
    https://t.me/CodefyChannel/40
    https://stepik.org/lesson/567054/step/2

    This function returns the greatest common divisor of two positive integers a and b.
    :param a: first number
    :param b: second number
    :return: greatest common divisor

    by @CodefyBot, t.me
    """
    while a != 0 and b != 0:
        if a > b:
            a = a % b
        else:
            b = b % a
    return a + b


print(get_nod(10, 15))

### <your text>
# Code:


### Write function on Python 3 that creates 1000 different random city names in list, getting cities name from internet, with docstrings.
# Code:

def get_city_name():
    """
    This function creates 1000 different random city names in list, getting cities name from internet.
    """
    url = 'https://randomuser.me/api/?results=1000'
    response = requests.get(url)
    data = json.loads(response.text)
    cities = []
    for i in range(1000):
        cities.append(data['results'][random.randint(0, len(data['results'])-1)]['location']['city'])
    return cities

print(get_city_name())
