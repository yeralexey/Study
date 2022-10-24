"""
Генерация последователности сочетаний букв из ascii_lowercase, с выводом пятидесяти из них в консоль. На основании
решения выше.

https://stepik.org/lesson/567071/step/8

полный конспект темы:
https://github.com/yeralexey/Study/blob/master/notabene.py
"""
from string import ascii_lowercase
(lambda a: [print(next(a), end=" ") for _ in range(50)])(i + j for i in ascii_lowercase for j in ascii_lowercase)