def get_prime():
    n = 1
    while True:
        n+=1
        for i in range(2, n):
            if n%i == 0:
                break
        else:
            yield n

prime = get_prime()

for _ in range(20): print(next(prime), end = " ")