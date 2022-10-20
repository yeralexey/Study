'''
    Python interactive summary of "Recursive functions" theme,
    course of study 'Добрый, добрый Python' by Sergey Balakirev.
    Examples and tasks.
Интерактивный Python конспект темы 'Рекурсивные функции',
курса 'Добрый, добрый Python', от Сергея Балакирева.
Примеры и задачи.

https://stepik.org/lesson/567058/

N.B. Нижеприведенные функции написаны в процессе и для обучения,
лично автором конспекта. Они проходят испытания на 20.10.2022, при
этом могут быть не оптимальными(идеальными) с точки зрения логики алгоритмов.
'''


def recursive(value):
    '''
        example of the way recursive funtion works
    пример работы рекурсивной функции
    https://youtu.be/dtzoBXL11oo?t=36 (with timecode,  с привязкой ко времени)

    полный конспект темы:
    https://github.com/yeralexey/Study/blob/master/stepik.org/recursion.py
    '''
    print(value)            # выводим значение на выходе из рекурсии
    if value < 4:           # условие продолжения рекурсии
        recursive(value+1)  # рекурсивно запускаем с увеличением значения
    print(value)            # выводим значение


def fact(n):
    '''
        counting factorial with recursive function
    вычисление факториала рекурсивной функцией
    https://youtu.be/dtzoBXL11oo?t=345 (with timecode,  с привязкой ко времени)

    полный конспект темы:
    https://github.com/yeralexey/Study/blob/master/stepik.org/recursion.py
    '''
    if n <= 0:               # определяем условие выхода из рекурсии
        return 1           # выход из функции
    else:
        return n*fact(n-1)  # рекурсивно запускаем подсчет


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
    '''
        creatitng and print file tree with recursive function,
        tree is set by dictionary, named "F", before this function
    создание и вывод дерева файлов рекурсивной функцией, пример дерева
    задан в переменной "F" перед самой функцией
    https://youtu.be/dtzoBXL11oo?t=558 (with timecode,  с привязкой ко времени)

    полный конспект темы:
    https://github.com/yeralexey/Study/blob/master/stepik.org/recursion.py
    '''
    for f in path:                            # для каждого элемента словаря
        print(" " * depth, f)                 # выводим значение со стартовым кол-вом пробелов (корневой каталог)
        if type(path[f]) is dict:             # если тип элемента - словарь
            get_files(path[f], depth + 1)     # рекурсивно запускаемся в нем, с увеличением пробелов
        else:
            print(" " * (depth + 1), " ".join(path[f]))  # если не словарь - выводим с увеличением отступа


def get_rec_N(N):
    '''
        print numbers from one to N with recursive function
    вывести числа от единицы до N рекурсивной функцией
    https://stepik.org/lesson/567058/step/3

    полный конспект темы:
    https://github.com/yeralexey/Study/blob/master/stepik.org/recursion.py
    '''
    if N > 0:              # задаем условие продолжения рекурсии
        get_rec_N(N - 1)   # запускаем рекурсивно с уменьшением значения
        print(N)           # выводим значение, углубляясь в рекурсию


def get_rec_sum(inpt, total):
    '''
        count inputed with string numbers with recursive function, print after
    сосчитать рекурсивной функцией сумму введенных строкой чисел, после вывести
    https://stepik.org/lesson/567058/step/4

    полный конспект темы:
    https://github.com/yeralexey/Study/blob/master/stepik.org/recursion.py
    '''
    num = next(inpt)                       # следующее значение из итератора
    if num != 1:                           # при условии что это не int(1), остальные str
        total = total + int(num)           # добавляем к результату значение
        return get_rec_sum(inpt, total)    # запускем рекурсию
    else:
        return total                       # возвращаем результат


def fib_rec(N, f=[1, 1]):  # ключевым параметром задаем первые два элемента последовательности
    '''
        create Fibonacci sequence, wint total values limited by input number
    сформировать последовательность Фиббоначи, количество значений в которой
    лимитировано вводимым натруральным числом
    https://stepik.org/lesson/567058/step/5

    полный конспект темы:
    https://github.com/yeralexey/Study/blob/master/stepik.org/recursion.py
    '''
    if len(f) < N:                     # если длинна списка меньше ограничивающего числа
        f.append(f[-1] + f[-2])        # добавляем к списку последовательности сумму двух последних элeментов
        return fib_rec(N, f=f)       # рекурсивно запускаем функцию
    else:
        return f

# ---------------------------------------------------------------


'''
Uncommented needed and run, works with "help" also, ex.: help(get_files)

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
# N = int(input())                              # ввод с клавиатуры
N = 8                                          # ввод тестового значения
get_rec_N(N)                                   # вызов функции
help(get_rec_N)                                # вывод описания функции

# #--- Задача 2
# inpt = input()                                # ввод с клавиатуры
inpt = '8 11 -5 4 3'                           # ввод тестового значения
inpt = iter([i for i in inpt.split()]+[1])     # преобразование в итератор
print(get_rec_sum(inpt, 0))                    # вывод результата функции
help(get_rec_sum)                              # вывод описания функции

# #--- Задача 3
# N = int(input())                              # ввод с клавиатуры
N = 14                                         # ввод тестового значения
print(fib_rec(N))                              # вывод результата функции
help(fib_rec)                                  # вывод описания функции
