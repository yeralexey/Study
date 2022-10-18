# Never tried to refactor, one of the implementations of this task:
# https://www.codewars.com/kata/63022799acfb8d00285b4ea0;
# counts four Lagrange squares for number up to 2**1024;
# not all cases of number resolved, fails sometimes, was written just to pass the task;
# for numbers 2^s * (2m+1), for example, script will simply loop;
# line 47 contains condition, that starts "fast algorythm for large numbers", can be decreased;
# described here https://t.me/yerinalexey/193, in russian.

# Contains the implementation of Miller-Rabin, not necessary to solve, just to practice.


import math
import random
from typing import Tuple


def four_squares(n: int) -> Tuple[int, int, int, int]:
    if n == 0:
        return 0, 0, 0, 0
        print("by zero")
    n_sq = math.isqrt(n)
    ramin = math.ceil(n_sq * 0.7)
    ramax = math.ceil(n_sq * 0.91)
    mark_a = 0
    i = 0
    while True:
        if mark_a == 0:
            try:
                a = random.randrange(ramin, ramax)
            except:
                a = n_sq
        a = a - mark_a
        if a == 0:
            a = random.randrange(ramin, ramax)
        a2 = a * a
        left = n - a2
        if left == 0:
            print("a000")
            return a, 0, 0, 0
        b = math.isqrt(left)
        b2 = b * b
        left = left - b2
        if left == 0:
            print("ab00")
            return a, b, 0, 0
        b_left = left
        if n > 2 ** 1000:  # I was just kidding, haha. But it works well for numbers up to 2**103.
            if b_left % 4 == 1:
                if b_left % 4 != 3:
                    if math.isqrt(b_left - 1) == n - a2 - b2 - 1:
                        print("by magic")
                        return a, b, math.isqrt(b_left - 1), 1
                    if millerrabin(b_left) == True:
                        cd = doFerma(b_left)
                        if cd != False:
                            return a, b, cd[0], cd[1]
        else:
            c = math.isqrt(left)
            c2 = c * c
            left = left - c2
            if left == 0:
                return a, b, c, 0
            d = math.isqrt(left)
            d2 = d * d
            if left - d2 == 0:
                return a, b, c, d
        if i % 50 == 0:
            mark_a = 0
        else:
            mark_a = 1
        i += 1


def millerrabin(num):  # This part is based on wikipedia's article. By the way, some implementations on github.com
    k = 4              # for python are simply wrong. This one was checked with gmpy2 solution.
    s = 0
    t = num - 1
    while t % 2 == 0:
        s += 1
        t = t // 2
    for ki in range(k):
        a = random.randrange(2, num - 2)
        x = pow(a, t, num)
        if x == 1 or x == num - 1:
            continue
        si = s - 1
        sc = True
        while sc == True:
            if si == 0:
                return False
            x = pow(x, 2, num)
            if x == 1:
                return False
            if x == num - 1:
                sc = False
            si -= 1
    return True


def doFerma(b_left):
    stop = False
    while stop == False:
        b = random.randrange(1, (b_left - 1) // 2)
        e = pow(b, (b_left - 1) // 4, b_left)
        if pow(e, 2, b_left) == b_left - 1:
            stop = True
    y_a = b_left
    f = b_left - e
    if f > e:
        y_b = e
    else:
        y_b = f
    t_n = math.sqrt(b_left)
    stop = False
    while stop == False:
        r_r = y_a % y_b
        if r_r < t_n:
            stop = True
        y_a = y_b
        y_b = r_r
    c = r_r
    d = math.isqrt(b_left - c * c)
    if b_left == c * c + d * d:
        return [c, d]
    else:
        return False

result = four_squares(random.randrange(2**1024, 2**1034)) # this lines are to be removed,
print(result)                                             # if to paste in codewars.