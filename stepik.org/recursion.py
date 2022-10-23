"""
    "Talk is cheap. Show me the code." (с) Linus Torvalds"

    Python interactive summary of "Recursive functions" theme,
    course of study "Добрый, добрый Python" by Sergey Balakirev.
    Examples and tasks.
Интерактивный Python конспект темы "Рекурсивные функции",
курса "Добрый, добрый Python", от Сергея Балакирева.
Примеры и задачи.

https://stepik.org/lesson/567058/

N.B. Нижеприведенные функции решений задач написаны в процессе и для обучения,
лично автором конспекта. Они проходят испытания на 20.10.2022, при
этом могут быть не оптимальными(идеальными) с точки зрения логики алгоритмов.
"""


def recursive(value):
    """
        example of the way recursive funtion works
    Пример работы рекурсивной функции.
    https://youtu.be/dtzoBXL11oo?t=36 (with timecode,  с привязкой ко времени)

    полный конспект темы:
    https://github.com/yeralexey/Study/blob/master/stepik.org/recursion.py
    """
    print(value)            # выводим значение на выходе из рекурсии
    if value < 4:           # условие продолжения рекурсии
        recursive(value+1)  # рекурсивно запускаем с увеличением значения
    print(value)            # выводим значение


def fact(n):
    """
        counting factorial with recursive function
    вычисление факториала рекурсивной функцией
    https://youtu.be/dtzoBXL11oo?t=345 (with timecode,  с привязкой ко времени)

    полный конспект темы:
    https://github.com/yeralexey/Study/blob/master/stepik.org/recursion.py
    """
    if n <= 0:               # определяем условие выхода из рекурсии
        return 1             # выход из функции
    else:
        return n*fact(n-1)   # рекурсивно запускаем подсчет


F = {
    'C:': {
        'Python39': ['python.exe', 'python.ini'],
        'Program Files': {
            'Java': ['README.txt', 'Welcome.html', 'java.exe'],
            'MATLAB': ['matlab.bat', 'matlab.exe', 'mcc.bat']
        },
        'Windows': {
            'System32': ['acledit.dll', 'aclui.dll', 'zipfldr.dll']
        }
    }
}


def get_files(path, depth=0):  # получаем путь, в нашем случае - словарь, ключевым параметром задано
                               # количество пробелов при отображении глубины вложенности
    """
        Creatitng and print file tree with recursive function,
        tree is set by dictionary, named "F", before this function.
    Создание и вывод дерева файлов рекурсивной функцией, пример дерева
    задан в переменной "F" перед самой функцией.
    https://youtu.be/dtzoBXL11oo?t=558 (with timecode,  с привязкой ко времени)

    полный конспект темы:
    https://github.com/yeralexey/Study/blob/master/stepik.org/recursion.py
    """
    for f in path:                            # для каждого элемента словаря
        print(" " * depth, f)                 # выводим значение со стартовым кол-вом пробелов (корневой каталог)
        if type(path[f]) is dict:             # если тип элемента - словарь
            get_files(path[f], depth + 1)     # рекурсивно запускаемся в нем, с увеличением пробелов
        else:
            print(" " * (depth + 1), " ".join(path[f]))  # если не словарь - выводим с увеличением отступа


def get_rec_N(N):
    """
        Print numbers from one to "N" with recursive function.
    Вывести числа от единицы до "N" рекурсивной функцией.
    https://stepik.org/lesson/567058/step/3

    полный конспект темы:
    https://github.com/yeralexey/Study/blob/master/stepik.org/recursion.py
    """
    if N > 0:              # задаем условие продолжения рекурсии
        get_rec_N(N - 1)   # запускаем рекурсивно с уменьшением значения
        print(N)           # выводим значение, углубляясь в рекурсию


def get_rec_sum(inpt, total):
    """
        Count inputed with string numbers with recursive function, print after.
    Сосчитать рекурсивной функцией сумму введенных строкой чисел, после вывести.
    https://stepik.org/lesson/567058/step/4

    полный конспект темы:
    https://github.com/yeralexey/Study/blob/master/stepik.org/recursion.py
    """
    num = next(inpt)                       # следующее значение из итератора
    if num != 1:                           # при условии что это не int(1), остальные str
        total = total + int(num)           # добавляем к результату значение
        return get_rec_sum(inpt, total)    # запускем рекурсию
    else:
        return total                       # возвращаем результат


def fib_rec(N, f=[1, 1]):  # ключевым параметром задаем первые два элемента последовательности
    """
        Create Fibonacci sequence, with total values, limited by input number.
    Сформировать последовательность Фибоначчи, количество значений в которой
    лимитировано вводимым натруральным числом.
    https://stepik.org/lesson/567058/step/5

    полный конспект темы:
    https://github.com/yeralexey/Study/blob/master/stepik.org/recursion.py
    """
    if len(f) < N:                     # если длинна списка меньше ограничивающего числа
        f.append(f[-1] + f[-2])        # добавляем к списку последовательности сумму двух последних элeментов
        return fib_rec(N, f=f)         # рекурсивно запускаем функцию
    else:
        return f


def fact_rec(n):
    """
        Counting factorial with recursive function.
    Вычисление факториала рекурсивной функцией.
    https://youtu.be/dtzoBXL11oo?t=345 (with timecode,  с привязкой ко времени)
    https://stepik.org/lesson/567058/step/6

    полный конспект темы:
    https://github.com/yeralexey/Study/blob/master/stepik.org/recursion.py
    """
    if n <= 0:                  # определяем условие выхода из рекурсии
        return 1                # выход из функции
    else:
        return n*fact_rec(n-1)  # рекурсивно запускаем подсчет


d = [1, 2, [True, False], ["Москва", "Уфа", [100, 101], ['True', [-2, -1]]], 7.89]


def get_line_list(d, a=[]):
    """
        Create one demention list from multidementional, given in "d" with recursive function.
    Рекурсивной функцей создать одномерный список из значений элементов списка "d", задан
    перед этой функцией.
    https://stepik.org/lesson/567058/step/7

    полный конспект темы:
    https://github.com/yeralexey/Study/blob/master/stepik.org/recursion.py
    """
    for item in d:                           # для каждого элемента в листе d
        if type(item) is list:               # если тип элемента - лист
            get_line_list(d[d.index(item)])  # рекурсивно запускаем эту функцию, передавая его индекс
        else:
            a.append(item)                   # если не лист - добавить в одномерный список
    return a                                 # вернуть результат


def get_path(N, f=[1, 2]):  # ключевым параметром задаем значения первых двух элементов
    """
        Cout amount of steps to get to "N" with recursive function, if possible
        steps are 1 and 2.
    "Лягушка прыгает вперед и может скакнуть либо на одно деление, либо сразу на два.
    Наша задача определить количество вариантов маршрутов, которыми лягушка может достичь
    риски под номером "N" (натуральное число N вводится с клавиатуры)."
    https://stepik.org/lesson/567058/step/8

    полный конспект темы:
    https://github.com/yeralexey/Study/blob/master/stepik.org/recursion.py
    """
    if len(f) < N:                     # лягушка не прыгает дальше риски N
        f.append(f[-1] + f[-2])        # добавляем к начальному списку сумму двух последних элeментов
        return get_path(N, f=f)        # рекурсивно запускаем функцию подсчета прыжков
    else:
        return f[-1]                   # возвращаем значение последнего элемента


def sort_merg(lst):
    """
        Implement merge sorting with recursive function.
    Реализовать сортировку слиянием через рекурсивную функцию.
    https://stepik.org/lesson/567058/step/10

    полный конспект темы:
    https://github.com/yeralexey/Study/blob/master/stepik.org/recursion.py
    """
    if len(lst) == 1:                            # условие выхода из рекурсии
        return lst                               # выход из рекурсии
    cent = len(lst)//2                           # поиск середины списка
    left_lst = sort_merg(lst[:cent])             # рекурсивный запуск на деление первой части
    right_lst = sort_merg(lst[cent:])            # рекурсивный запуск на деление второй части
    return combine_lst(left_lst, right_lst, [])  # запуск функции слияния списков


def combine_lst(lst_a, lst_b, comb):
    if len(lst_a+lst_b) > 0:                        # пока в списках что то есть
        a, b = lst_a[:1], lst_b[:1]                 # присвоим значения срезами, на случай пустого
        if a and a >= b: comb.append(lst_a.pop(0))  # добавляем в список слияния большее
        if b and b >= a: comb.append(lst_b.pop(0))  # добавляем в список слияния большее
        return combine_lst(lst_a, lst_b, comb)      # рекурсивно запускаем повтор
    else:
        return comb                                 # возвращаем комбинированый список


# ---------------------------------------------------------------


'''
Uncomment needed and run, works with "help" also, ex.: help(get_files)

Раскомментируйте нужное и запускайте, работает запуск с "help", прим.: help(get_files)
'''

# # --- Пример 1
recursive(1)                            # вызов функции
help(recursive)                         # вывод описания функции

# # --- Пример 2
print(fact(6))                          # вывод результата функции
help(fact)                              # вывод описания функции

# # --- Пример 3
get_files(F)                            # вызов функции
help(get_files)                         # вывод описания функции


# # --- Задача 1
# N = int(input())                             # ввод с клавиатуры
N = 8                                          # ввод тестового значения
get_rec_N(N)                                   # вызов функции
help(get_rec_N)                                # вывод описания функции

# #--- Задача 2
# inpt = input()                               # ввод с клавиатуры
inpt = '8 11 -5 4 3'                           # ввод тестового значения
inpt = iter([i for i in inpt.split()]+[1])     # преобразование в итератор
print(get_rec_sum(inpt, 0))                    # вывод результата функции
help(get_rec_sum)                              # вывод описания функции

# #--- Задача 3
# N = int(input())                             # ввод с клавиатуры
N = 14                                         # ввод тестового значения
print(fib_rec(N))                              # вывод результата функции
help(fib_rec)                                  # вывод описания функции

# # --- Задача 4
# n = int(input())                             # ввод с клавиатуры
n = 11                                         # ввод тестового значения
print(fact_rec(n))                             # вывод результата функции
help(fact_rec)                                 # вывод описания функции

# # --- Задача 5
print(get_line_list(d))                        # вывод результата функции
help(get_line_list)                            # вывод описания функции

# # --- Задача 6                               # подходит решение с Фибоначчи
# N = int(input())                             # ввод с клавиатуры
N = 7                                          # ввод тестового значения
print(get_path(N))                             # вывод результата функции
help(get_path)                                 # вывод описания функции

# # --- Задача 7                               #
# # lst = [int(i) for i in input().split()]    # ввод с клавиатуры
lst = [8, 11, -6, 3, 0, 1, 1]                  # ввод тестового значения
print(print(*sort_merg(lst)[::-1]))            # вывод результата функции
help(sort_merg)                                # вывод описания функции
