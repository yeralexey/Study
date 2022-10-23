"""
Интересные примеры кода.

Составлено для личного пользования и запоминания.
"""


def filter_lst(it, key=None):
    """
    Функция типа lambda как фильтр, список фильтров помещен в кортеж, для демострации
    возможности подобного.

    https://stepik.org/lesson/567059/step/7
    """
    if key is None:
        return tuple(it)
    res = ()
    for x in it:
        if key(x):
            res += (x,)
    return res


filt = (lambda y: y < 0,
        lambda y: y >= 0,
        lambda y: 3 <= y <= 5)

# # inpt = input()
# inpt = '5 4 -3 4 5 -24 -6 9 0'
# inpt = [int(i) for i in inpt.split()]
# print(*filter_lst(inpt))
# print(*filter_lst(inpt, key=filt[0]))
# print(*filter_lst(inpt, key=filt[1]))
# print(*filter_lst(inpt, key=filt[2]))
print(help(filter_lst))


def input_while_q():
    """
    Пользователь с клавиатуры вводит названия городов, пока не введет букву q.
    Определить общее уникальное число городов, которые вводил пользователь. На
    экран вывести это число. Из коллекций при реализации программы использовать
    только множества.

    https://stepik.org/lesson/567049/step/9?thread=solutions&unit=561323
    https://stepik.org/lesson/567049/step/9
    """
    print(len(set(iter(input, 'q'))))

# input_while_q()
help(input_while_q)


def show_sorted(func):
    """
    Пример декоратора с использованием вложенной lambda функции, взято из задачи
    по созданию декоратора для возрата отсортированного списка, решение
    by Алекс Глозман.

    https://stepik.org/lesson/567062/step/4?thread=solutions&unit=561336

    """
    return lambda *args, **kwards: sorted(func(*args, **kwards))

@show_sorted
def get_list(s):
    return list(map(int, s.split()))

# print(*get_list("8 11 -5 4 3 10"))
help(show_sorted)
