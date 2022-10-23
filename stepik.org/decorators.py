"""
    "Talk is cheap. Show me the code." (с) Linus Torvalds

Декораторы. Интерактивный конспект Python.

на осннове лекций :
Олега Молчанова   - https://www.youtube.com/watch?v=Ss1M32pp5Ew
Ивана Викторовича - https://www.youtube.com/watch?v=3WbglY2b65g&list=PLs2IpQwiXpT3SqbqPzLCEy1fow9G7g0oY&index=20
Сергея Балакирева - https://www.youtube.com/watch?v=v0qZPplzwUQ
                  - https://youtu.be/bl_CnIVpWmQ

Приведен код из видео, а так же решены задачи тем 7.11 "Декораторы функций", 7.12 "Передача аргументов декораторам"
курса "Добрый, добрый Python" Сергея Балакирева.
https://stepik.org/lesson/567062/step/1
https://stepik.org/lesson/567063/step/1

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


# @timeit('name')                # "синтаксический сахар" с аргументом, выводит ('name',) в консоль, !снять комментарий!
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

    https://stepik.org/lesson/567062/step/1
    """

    def wraper(*args, **kwargs):          # выполняет блок команд до и после оборачиваемой функции
        print("---  some actions ---")    # вывод до выполнения оборачиваемой функции
        result = func(*args, **kwargs)    # выполнение оборачиваемой функции
        print("---  some actions ---")    # вывод после выполнения оборачиваемой функции
        return result                     # возврат переменной result
    return wraper                         # возврат результата функции wrapper


def some_func(title, tag):                    # оборачиваемая функция
    print(f"title = {title}, tag = {tag}")    # вывод аргументов оборачиваемой функции
    return f"<{tag}>{title}</{tag}>"          # возврат оборачиваемой функции


# help(func_decorator)
# f = func_decorator(some_func)  # присвоение объекта функции переменной f и передача функции в декоратор
# tagged = f("python", "h1")     # вызов оборачиваемой фунции с аргументами и декоратором, присвоение результата tagged
# print(tagged)                  # вывод содержания tagged


import time


def test_time(func):
    """
    Имплементация подсчета времени выполнения функции от Сергея Балакирева, сравнение
    нахождения общего делителя по быстрому и медленному алгоритмам Евклида.

    Код из видео Сергея Балакирева
    https://www.youtube.com/watch?v=v0qZPplzwUQ

    https://stepik.org/lesson/567062/step/1
    """

    def wraper(*args, **kwargs):        # выполняет блок команд до и после оборачиваемой функции
        st = time.time()                # timestamp начала работы
        result = func(*args, **kwargs)  # выполнение оборачиваемой функции
        et = time.time()                # timestamp завершения работы
        dt = et - st                    # timestamp начала - timestamp завершения
        print(f"time: {dt} sek")        # вывод разницы во времени
        return result                   # возврат результата функции wrapper

    return wraper


@test_time
def get_nod_fast(a, b):              # быстрый алгорим Евклида по нахождению НОД
    while b > 0: a, b = b, a % b     # пока b больше ноля - a равно b, b равно отстатку от деления a на b
    return a                         # вернуть a


@test_time
def get_nod_slow(a, b):             # медленный алгорим Евклида по нахождению НОД
    while a != b:                   # пока b не равно a
        if a > b:                   # если a больше b
            a -= b                  # a равно a минус b
        else:                       # иначе
            b -= a                  # b равно b минус a
    return a                        # вернуть a


# help(test_time)
# get_nod_slow = test_time(get_nod_slow)(2, 1000000) # вариант запуска без указания декоратора над функцией
# get_nod_fast = test_time(get_nod_fast)(2, 1000000) # вариант запуска без указания декоратора над функцией
# res1 = get_nod_slow(2, 1000000) # вариант запуска с указанием декоратора над функцией
# res2 = get_nod_fast(2, 1000000) # вариант запуска с указанием декоратора над функцией
# print(res1, res2)               # вывод НОД для запуска с указанием декоратора над функцией


from functools import wraps    # импорт дублируется в конспекте, но по условиям задачи
import math


def df_decorator(dx=0.01):  # параметры декоратора передатся через дополнительное вкладывание
    """
    Декоратор для вычисления производной функции c передачей параметра декоратора

    Код из видео Сергея Балакирева
    https://youtu.be/bl_CnIVpWmQ

    https://stepik.org/lesson/567063/step/1
    """

    def func_decorator(func):
        @wraps(func)   # данный дкоратор сохраняет имя оборачиваемой функциии
        def wrapper(x, *args, **kwargs):
            res = (func(x + dx, *args, **kwargs) - func(x, *args, **kwargs)) / dx  # вычисление производной
            return res
        # wrapper.__name__ = func.__name__      # аналог декоратора @wraps
        # wrapper.__doc__ = func.__doc__        # аналог декоратора @wraps
        return wrapper
    return func_decorator


@df_decorator(dx=0.001)
def sin_df(x):
    """
    Описание функции sin_df()
    :param x: число
    :return: синус числа
    """
    return math.sin(x)


# print(help(df_decorator))
# f = df_decorator(dx=0.001)          # вызов без обращения к упоминанию декоратора над функцией(там должен стоять "#")
# sin_df = f(sin_df)
# # или
# f = df_decorator(dx=0.001)(sin_df)  # вызов без обращения к упоминанию декоратора над функцией(там должен стоять "#")
# или

# df = sin_df(math.pi/3)                # вызов с синтаксическим сахаром
# print(df)
# print(sin_df.__name__)                # вывод имени оборачиваемой функции
# print(sin_df.__doc__)                 # вывод описания оборачиваемой функции


def func_show(func):                    # объявляем функцию декоратор
    """
    Декоратор вывода значений функции подсчета площади прямоугольника.

    https://stepik.org/lesson/567062/step/2

    полный конспект темы:
    https://github.com/yeralexey/Study/blob/master/stepik.org/decorators.py

    """
    def wrapper(*args, **kwargs):                    # функция, которая выполняет блок команд
        result = func(*args, **kwargs)               # запускаем оборачиваемую функцию
        print(f'Площадь прямоугольника: {result}')   # выводим результат согласно задания
    return wrapper                                   # возвращаем результат блока команд (запускаем)


@func_show                             # N.B. применять декоратор функции так же не нужно, т.е. каммент.
def get_sq(width, height):             # объявляем функцию вычисления площади
    return width*height                # возвращаем вычисление площади


# help(func_show)
# get_sq(5, 7)                           # запуск функции с тестовыми аргументами


def show_menu(func):
    """
    Декоратор вывода преобразовыванного ввода из строк в список в формате:
    1. Пункт_1
    2. Пункт_2
    ...
    N. Пункт_N

    https://stepik.org/lesson/567062/step/3

    полный конспект темы:
    https://github.com/yeralexey/Study/blob/master/stepik.org/decorators.py
    """
    def wrapper(*args):                                       # функция, которая выполняет блок команд
        menu = func(*args)                                    # запускаем оборачиваемую функцию
        [print(f"{i+1}. {j}") for i, j in enumerate(menu)]    # выводим результат согласно задания
    return wrapper                                            # возвращаем результат блока команд (запускаем)


@show_menu                        # применяем декоратор
def get_menu(s):                  # объявляем функцию
    return s.split()              # превращаем в список


# help(show_menu)
# inpt = input()                            # ввод с клавиатуры
# inpt = "Главная Добавить Удалить Выйти"   # тестовый ввод
# get_menu(inpt)                            # вызов (при решении на платформе - не нужен)


def sort_inpt(func):
    """
    Сортировка декоратором ввода, преобразованного из строки в список чисел.

    https://stepik.org/lesson/567062/step/4

    полный конспект темы:
    https://github.com/yeralexey/Study/blob/master/stepik.org/decorators.py
    """
    def wrapper(*args):                      # функция, которая выполняет блок команд
        return sorted(func(*args))           # вызываем обрачиваемую функцию и сортируем результат
    return wrapper                           # возвращаем результат блока команд (запускаем)


@sort_inpt                                # применяем декоратор
def get_list(l):                          # объявляем функцию
    return [int(i) for i in l.split()]    # превращаем в список


# help(sort_inpt)
# inpt = input()                          # ввод с клавиатуры
# inpt = "8 11 -5 4 3 10"                 # тестовый ввод
# print(*get_list(inpt))                  # вызов и вывод


def dict_it(func):
    """
    Формирование словаря из двух списков декоратором, без zip и цикла, применен
    итератор.

    https://stepik.org/lesson/567062/step/5

    полный конспект темы:
    https://github.com/yeralexey/Study/blob/master/stepik.org/decorators.py
    """
    def wrapper(a, b):
        lst_a, lst_b = func(a, b); it_b = iter(lst_b)  # получаем списки из ф-ции, значения преобразуем в итератор
        return {i: next(it_b) for i in lst_a}         # формируем список генератором, итерируя values
    return wrapper


@dict_it
def get_lists(a, b):              # объявление функции
    return a.split(), b.split()   # преобразование параметров в списки и возврат


# help(dict_it)
# vol1 = input()                      # ввод с клавиатуры первой строки
# vol2 = input()                      # ввод с клавиатуры первой строки
# vol1 = 'house river tree car'       # тестовый ввод первой строки
# vol2 = 'дом река дерево машина'     # тестовый ввод второй строки
# d = get_lists(vol1, vol2)           # запуск функции, получение d
# print(*sorted(d.items()))           # вывод результата согласно заданию


t = {'ё': 'yo', 'а': 'a', 'б': 'b', 'в': 'v', 'г': 'g', 'д': 'd', 'е': 'e', 'ж': 'zh',
     'з': 'z', 'и': 'i', 'й': 'y', 'к': 'k', 'л': 'l', 'м': 'm', 'н': 'n', 'о': 'o', 'п': 'p',
     'р': 'r', 'с': 's', 'т': 't', 'у': 'u', 'ф': 'f', 'х': 'h', 'ц': 'c', 'ч': 'ch', 'ш': 'sh',
     'щ': 'shch', 'ъ': '', 'ы': 'y', 'ь': '', 'э': 'e', 'ю': 'yu', 'я': 'ya'}


def strip_excess(func):
    """
    Декоратор удаления избыточных дефисов для преобразующей кириллицу в латинницу
    функции, дополнительно заменяющей ": ;.,_" => "-", на базе lambda.

    https://stepik.org/lesson/567062/step/5

    полный конспект темы:
    https://github.com/yeralexey/Study/blob/master/stepik.org/decorators.py
    """
    return lambda *args: func(*args).replace("---", "-")  # делает вышесказанное :)


@strip_excess
def invert_english(s, t):
    items = ": ;.,_"                                    # строка с доп сиволами из задания
    t = {**dict.fromkeys(items, "-"), **t}              # дополнена в словарь
    return "".join([t[i] if i in t else i for i in s])  # возвращаем преобразованную строку


# help(strip_excess)
# s = input()                              # ввод с клавиатуры
# s = "Python - это круто!"                # тестовый ввод
# print(invert_english(s.lower(), t))      # запуск тестового ввода


def add_smth(num):
    """
    Декоратор функции, получающей сумму из строки с числами,
    добавляющий аргумент.

    https://stepik.org/lesson/567063/step/2

    полный конспект темы:
    https://github.com/yeralexey/Study/blob/master/stepik.org/decorators.py
    """
    def outer(func):                 # принимает объект функции
        def wrapper(s_s):            # принимает агрумент функции
            res = func(s_s) + num    # вызывает функцию и складывает с аргументом декоратора
            return res               # wrapper возвращает результат
        return wrapper               # возврат wrapper
    return outer                     # возврат outer


@add_smth(5)                                 # подключение декоратора
def get_sum(s):                              # объявление функции
    return sum([int(i) for i in s.split()])  # возврат суммы значений в строке


# help(get_sum)
# s = input()            # ввод с клавиатуры
# s = "5 6 3 6 -4 6 -1"  # тестовый ввод
# print(get_sum(s))      # вывод результата функции


def tag_decor(tag):
    """
    Декоратор для функции, переводящей введенную строку в нижний регистр, принимающий
    тег в качестве аргумента и оборачивающий в него строку.

    https://stepik.org/lesson/567063/step/3

    полный конспект темы:
    https://github.com/yeralexey/Study/blob/master/stepik.org/decorators.py
    """
    def outer(func):
        return lambda *args, **kwargs: f"<{tag}>{func(*args, **kwargs)}</{tag}>"
    return outer


@tag_decor(tag="div")
def lower_str(s):
    return s.lower()

# help(tag_decor)
# s = "Декораторы - это классно!"
# s = input()
# print(lower_str(s))


def strip_excess2(chars='!?'):  # декоратор с начальным параметром
    """
    Декоратор с параметром "?!:;,. ",  => "-" и "--" или "---" => "-",
    для функции, меняющей кириллическое написание на латинницу.

    https://stepik.org/lesson/567063/step/4

    полный конспект темы:
    https://github.com/yeralexey/Study/blob/master/stepik.org/decorators.py
    """
    def outer(func):                             # получаем функцию
        def wrapper(string):                     # получаем строку
            d_c = dict.fromkeys(chars, "-")      # словарь из символов в параметре
            result = "".join([d_c[i] if i in d_c else i for i in func(string)])  # замена символов из параметра
            while "--" in result: result = result.replace("--", "-")             # удаление лишних дефисов циклом
            return result
        return wrapper
    return outer


@strip_excess2(chars="?!:;,. ") # аргумент декоратора
def invert_english2(s):         # словарь поместил в функцию, тк. в конспекте есть аналогичный
    t2 = {'ё': 'yo', 'а': 'a', 'б': 'b', 'в': 'v', 'г': 'g', 'д': 'd', 'е': 'e', 'ж': 'zh',
         'з': 'z', 'и': 'i', 'й': 'y', 'к': 'k', 'л': 'l', 'м': 'm', 'н': 'n', 'о': 'o', 'п': 'p',
         'р': 'r', 'с': 's', 'т': 't', 'у': 'u', 'ф': 'f', 'х': 'h', 'ц': 'c', 'ч': 'ch', 'ш': 'sh',
         'щ': 'shch', 'ъ': '', 'ы': 'y', 'ь': '', 'э': 'e', 'ю': 'yu', 'я': 'ya'}
    return "".join([t2[i] if i in t else i for i in s])  # возвращаем преобразованную строку


# help(strip_excess2)
# s = input()                                # ввод с клавиатуры
# s = "Декораторы - это круто!!!!!!!"        # тестовый ввод
# print(invert_english2(s.lower()))          # вывод результата функции


from functools import wraps  # импорт дублируется в конспекте, но по условиям задачи


def summ_it(func):
    """
    Декоратор, суммирующий результат функции, преобразующий
    введенную строку в список чисел, с применением @wraps для
    сохранения свойств __doc__, __name__.

    https://stepik.org/lesson/567063/step/5

    полный конспект темы:
    https://github.com/yeralexey/Study/blob/master/stepik.org/decorators.py
    """
    @wraps(func)                   # сохраняем свойства оборачиваемой ф-ции
    def wrapper(int_lst):          # получаем список чисел
        return sum(func(int_lst))  # суммируем, возвращаем
    return wrapper                 # возвращаем  wrapper


@summ_it
def get_list2(string):      #  переименовать в  get_list!!!
    '''Функция для формирования списка целых значений'''
    return [int(i) for i in string.split()]  # cтрока => список чисел


# inpt = "2 3 5 6 7 8 4"           # тестовый ввод
# print(get_list2(inpt))           # проверка работы ф-ции
# print(get_list2.__doc__)         # проверка локального свойства