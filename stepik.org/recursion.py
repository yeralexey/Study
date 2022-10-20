'''
Python interactive summary of "Recursive functions" theme,
course of study 'Добрый, добрый Python' by Sergey Balakirev.

Examples and tasks.

Интерактивный Python конспект темы 'Рекурсивные функции',
курса 'Добрый, добрый Python', от Сергея Балакирева.

Примеры и задачи.

https://stepik.org/lesson/567058/
'''


def recursive(value):
    '''
    example of the way recursive funtion works

    пример работы рекурсивной функции

    https://youtu.be/dtzoBXL11oo?t=36 (with timecode,  с привязкой ко времени)

    полный конспект темы:
    https://github.com/yeralexey/Study/blob/master/stepik.org/recursion.py
    '''
    print(value)           # выводим значение на выходе из рекурсии
    if value < 4:          # условие продолжения рекурсии
        recursive(value+1) # рекурсивно запускаем с увеличением значения
    print(value)           # выводим значение


def fact(n):
    '''
    counting factorial with recursive function

    вычисление факториала рекурсивной функцией

    https://youtu.be/dtzoBXL11oo?t=345 (with timecode,  с привязкой ко времени)

    полный конспект темы:
    https://github.com/yeralexey/Study/blob/master/stepik.org/recursion.py
    '''
    if n<=0:               # определяем условие выхода из рекурсии
        return 1           # выход из рекурсии
    else:
        return n*fact(n-1) # рекурсивно запускаем подсчет


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


#---------------------------------------------------------------

'''
Uncommented and run, works with "help" also, ex.: help(get_files)

Раскомментируйте и запускайте, работает запуск с "help", прим.: help(get_files)
'''


#recursive(1)
 #help(recursive)

#print(fact(6))
 #help(fact)

#get_files(F)
 #help(get_files)

#get_rec_N(5)
 #help(get_rec_N)

