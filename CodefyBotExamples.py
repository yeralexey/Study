"""
Interesting generations by https://t.me/CodefyBot after testedin main.py
"""

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