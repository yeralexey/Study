from string import ascii_lowercase
(lambda a: [print(next(a)) for _ in range(4)])(i+j for i in ascii_lowercase for j in ascii_lowercase)
