"""
    "Болтовня ничего не стоит. Покажите мне код" (с) Linus Torvalds

Декораторы. Интерактивный конспект Python.

на осннове лекций :
Олега Молчанова   - https://www.youtube.com/watch?v=Ss1M32pp5Ew
Ивана Викторовича - https://www.youtube.com/watch?v=3WbglY2b65g&list=PLs2IpQwiXpT3SqbqPzLCEy1fow9G7g0oY&index=20
Сергея Балакирева - https://www.youtube.com/watch?v=v0qZPplzwUQ

Приведен код из видео, а так же решены задачи темы 7.11 "Декораторы функций" курса "Добрый, добрый Python"
Сергея Балакирева.
https://stepik.org/lesson/567062/step/1?unit=561336

N.B. Нижеприведенные функции решений задач написаны в процессе и для обучения,
лично автором конспекта. Они проходят испытания на 22.10.2022, при
этом могут быть не оптимальными(идеальными) с точки зрения логики алгоритмов.
"""

from datetime import datetime


def timeit(*args):                         # принимает агрумент декоратора
    """
    Функция - декоратор, измеряющая время работы декорируемой функции.
    В приведенном примере сравнивает скорость формирования списка (type 'list')
    циклом for и генератором, формирование происходит в функциях  one, two.

    Код из видео Олега Молчанова
    https://www.youtube.com/watch?v=Ss1M32pp5Ew

    Дополнительные тезисы:
    - функция должна содержать только целевой код;
    - dry, don't repeat yourself;
    - функции - объекты первого класса;
    """
    print(args)

    def outer(func):                        # принимает функцию
        def wrapper(*args, **kwargs):
            start = datetime.now()          # timestamp начала работы
            result = func(*args, **kwargs)  # выполняет переданную в декоратор функцию
            print(datetime.now() - start)   # завершение работы - timestamp начала
            return result                   # возврат результата работы переданной в декоратор ф-ции
        return wrapper                      # возврат wrapper
    return outer                            # возврат outer

# @timeit('name')                      # вызов осуществляется без
def one(n):
    # start = datetime.now()           # timestamp начала работы
    l = []                             # объявляем список
    for i in range(n):                 # формирование списка циклом
        if i % 2 == 0:                 # проверка на положительное число
            l.append(i)                # добавление в список
    # print(datetime.now() - start)    # завершение работы - timestamp начала
    return l


# @timeit('name')               # "синтаксический сахар" с аргументом, выводит ('name',) в консоль, !снять комментарий!
def two(n):
    # start = datetime.now()                 # timestamp начала работы
    l = [x for x in range(n) if x % 2 == 0]  # формирование списка генератором
    # print(datetime.now() - start )         # завершение работы - timestamp начала
    return l


# help(timeit)
# l1 = timeit('name')(one)(10**4)   # => wrapper(10) => one(10) # вызов декоратора без @timeit
# l2 = two(10**4)                   # вызов декоратора с @timeit
# print(l1)
# print(l2)
#
# l2_2 = two                        # обращение к функции two как к объекту
# print(type(l2_2), l2_2.__name__)  # вывод <class 'function'> wrapper, содержание, тип, имя


def my_decor(func):
    """
    Пример вывода текста в последовательности. В видео был и пример с измерением времени функции,
    идентичный с предыдущим.

    Код из видео Ивана Викторовича
    https://www.youtube.com/watch?v=3WbglY2b65g&list=PLs2IpQwiXpT3SqbqPzLCEy1fow9G7g0oY&index=20

    Дополнительные тезисы:
    - декоратор это функция, позволяющая обернуть другую функцию для расширения ее функциональности без
    непосредственного изменения кода оборачиваемой функции;
    - функция в Python это объект, мы можем проводить с функцией любые манипуляции как с объектом;
    - часто применяется дл разграничения прав пользователей в backend - Flask, Django
    - позволяет упростить код для повторяющихся действий
    - скрыть выполнение определенных функций
    """
    def wrapper(n):         # получаем арумент для основной функции
        print('start')      # перед выполнением
        func(n)             # выполнение основной ф-ции
        print('stop')       # после выполнения
    return wrapper          # возврат значения wrapper

@my_decor
def my_func(number):              # основная функция для передачи в декоратор
    print(number**2)              # возведение в квадрат


# help(my_decor)
# my = my_decor(my_func); my(10)  # вариант вывода без указания декоратора над функцией
# my_func(10)                     # вариант вывода с указанием декоратора над функцией


def func_decorator(func):
    """
    Пример, иллюстрирующий порядок выполнения декоратора и декорируемой функции,
    с передачей в функцию строки, тега, выводом строки внутри тегов.

    Код из видео Сергея Балакирева
    https://www.youtube.com/watch?v=v0qZPplzwUQ

    Дополнительные тезисы:
    -

    """

    def wraper(*args, **kwargs):
        print("---  some actions ---")
        result = func(*args, **kwargs)
        print("---  some actions ---")
        return result
    return wraper


def some_func(title, tag):
    print(f"title = {title}, tag = {tag}")
    return f"<{tag}>{title}</{tag}>"


f = func_decorator(some_func)
tagged = f("python", "h1")
print(tagged)