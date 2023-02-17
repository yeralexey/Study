"""
Unfinished!!!
what was done
https://www.codewars.com/kata/638c92b10e43cc000e615a07/
"""
import random
import time
import logging
from logging import handlers


logger = logging.getLogger("primes")
file_handler = logging.handlers.RotatingFileHandler(filename="primes.log", maxBytes=1000000,
                                                    backupCount=5)
console_handler = logging.StreamHandler()
console_handler.setLevel(level="DEBUG")
logger.addHandler(file_handler)
logger.setLevel(level="DEBUG")
logger.addHandler(console_handler)


def miller_rabin(n, k):
    if n == 2:
        return True
    if not n & 1:
        return False

    def check(a, s, d, n):
        x = pow(a, d, n)
        if x == 1:
            return True
        for i in range(s - 1):
            if x == n - 1:
                return True
            x = pow(x, 2, n)
        return x == n - 1

    s = 0
    d = n - 1

    while d % 2 == 0:
        d >>= 1
        s += 1

    for i in range(k):
        a = random.randrange(2, n - 1)
        if not check(a, s, d, n):
            return False
    return True


def primes_eratosphen(n):
    if n < 3:
        return []

    primes = [2]
    sieve = [True] * (n // 2)
    limit = int(n ** 0.5)

    for i in range(1, limit // 2 + 1):
        if sieve[i]:
            p = 2 * i + 1
            primes.append(p)
            for j in range(2 * i * (i + 1), len(sieve), p):
                sieve[j] = False

    for i in range(limit // 2 + 1, len(sieve)):
        if sieve[i]:
            primes.append(2 * i + 1)

    return primes


def primes_atkin(n):
    if n < 3:
        return []

    primes = [2, 3]
    sieve = [False] * (n + 1)
    limit = int(n ** 0.5)

    for x in range(1, limit + 1):
        for y in range(1, limit + 1):
            num = 4 * x**2 + y**2
            if num <= n and (num % 12 == 1 or num % 12 == 5):
                sieve[num] = not sieve[num]

            num = 3 * x**2 + y**2
            if num <= n and num % 12 == 7:
                sieve[num] = not sieve[num]

            num = 3 * x**2 - y**2
            if x > y and num <= n and num % 12 == 11:
                sieve[num] = not sieve[num]

    for num in range(5, limit):
        if sieve[num]:
            for multiple in range(num**2, n + 1, num**2):
                sieve[multiple] = False

    for i in range(5, n):
        if sieve[i]:
            primes.append(i)

    return primes



def primes_sundaram(n):
    if n < 2:
        return []

    k = (n - 2) // 2
    sieve = [False] * (k + 1)

    for i in range(1, k + 1):
        j = i
        while i + j + 2*i*j <= k:
            sieve[i + j + 2*i*j] = True
            j += 1

    primes = [2] + [2*i+1 for i in range(k) if not sieve[i]]

    return primes

def count_primes_less_than_wiliams(n) :
    """
    https://www.geeksforgeeks.org/solution-get-prime-numbers-smaller-n/
    """
    fact = 1
    count = 0
    for k in range(2, n):
        fact = fact * (k - 1)
        if ((fact + 1) % k == 0):
            count+=1
    return count



def count_primes_less_than(n):
    timemark = time.time()

    # logger.info("\nEratosphen"); list_of_primes = primes_eratosphen(n)
    # logger.info("\nAtkin"); list_of_primes = primes_atkin(n)
    logger.info("\nSundaram"); list_of_primes = primes_sundaram(n)

    logger.info(f'start counting sieve at -  {time.time() - timemark}')
    amount = len(list_of_primes)
    logger.info(f'amount - {amount}')
    logger.info(f'start checking with miller-rabin at -  {time.time() - timemark}')

    count = 0
    for i in list_of_primes:
        if i < 5:
            count+=1
        elif miller_rabin(i, 10):
            count+=1

    logger.info(f'finished at -  {time.time() - timemark}')

    return count



logger.info(f"total - {count_primes_less_than(10_000_000)}")
logger.info(f"total - {count_primes_less_than(10_000_000)}")
logger.info(f"total - {count_primes_less_than(10_000_000)}")
logger.info(f"total - {count_primes_less_than(10_000_000)}")