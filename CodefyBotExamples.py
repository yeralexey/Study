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


#checks if Tic-Tac_Toe solved.
#Receive board 3x3 array, value is 0 if empty, 1 if it is "X", or 2 if it is an "O" .
#Return -1 if board not finished AND no one has won, 1 if "X" won, 2 if "O" won, 0 if it's a cat's. Name is_solved


def is_solved(board):
    """
    https://t.me/CodefyChannel/45
    https://www.codewars.com/kata/525caa5c1bf619d28c000335/ - 5 kye

    Function checks if Tic-Tac_Toe solved.
    :param board: 3x3 array, value is 0 if empty, 1 if it is "X", or 2 if it is an "O"
    :return: -1 if board not finished AND no one has won, 1 if "X" won, 2 if "O" won, 0 if it's a cat's

    by @CodefyBot, t.me
    """
    # Checking rows
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] != 0:
            return board[i][0]
    # Checking columns
    for i in range(3):
        if board[0][i] == board[1][i] == board[2][i] != 0:
            return board[0][i]
    # Checking diagonals
    if board[0][0] == board[1][1] == board[2][2] != 0:
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] != 0:
        return board[0][2]
    # Checking if board is full
    for i in range(3):
        for j in range(3):
            if board[i][j] == 0:
                return -1
    return 0


# How to call example:
board = [[1, 2, 1],
         [2, 1, 2],
         [2, 1, 2]]
print(is_solved(board))