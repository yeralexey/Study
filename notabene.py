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
    if key is None:      # если функция вызвана без передачи lambda фильтра
        return tuple(it) # вернуть кортеж из данных в параметре it
    res = ()             # объявляем пустой кортеж
    for x in it:         # для каждого элемента объекта из параметра it
        if key(x):       # если lambda в параметре key возвращает True
            res += (x,)  # новый кортеж из старого сложенный с данным элементом
    return res


filt = (lambda y: y < 0,         # для y в lambda, если y меньше ноля...
        lambda y: y >= 0,
        lambda y: 3 <= y <= 5)


# help(filter_lst)
# inpt = '5 4 -3 4 5 -24 -6 9 0'
# inpt = [int(i) for i in inpt.split()]
# print(*filter_lst(inpt))
# print(*filter_lst(inpt, key=filt[0]))
# print(*filter_lst(inpt, key=filt[1]))
# print(*filter_lst(inpt, key=filt[2]))


def input_while_q():
    """
    Пользователь с клавиатуры вводит названия городов, пока не введет букву q.
    Определить общее уникальное число городов, которые вводил пользователь. На
    экран вывести это число. Из коллекций при реализации программы использовать
    только множества.

    https://stepik.org/lesson/567049/step/9
    """
    print(len(set(iter(input, 'q'))))


# help(input_while_q)
# input_while_q()


def show_sorted(func):
    """
    Пример декоратора с использованием вложенной lambda функции, взято из задачи
    по созданию декоратора для возрата отсортированного списка, решение
    by @Алекс_Глозман.

    https://stepik.org/lesson/567062/step/4

    """
    return lambda *args, **kwards: sorted(func(*args, **kwards))

@show_sorted
def get_list(s):
    return list(map(int, s.split()))


# help(show_sorted)
# print(*get_list("8 11 -5 4 3 10"))


def open_close_file():
    """
    Конструкция для работы с файлом, максимально учитывающая безопасность
    работы с данными от Сергея Балакирева.

    https://youtu.be/tM5qE8YLLuo
    """
    try:
        with open("my_file.txt", encoding="utf-8") as file: # открытие на чтение, или...
            s = file.readlines()                            # чтение построчно, или...
            int(s)                                          # имитация ошибки
    except FileNotFoundError:                               # обработка изключения "файл не найден"
        print("Невозможно открыть файл")
    except:
        print("Ошибка при работе с файлом")


# help(open_close_file)
# open_close_file()


def lambda_input():
    """
    Получение ввода функцией lambda c одновременным присвоением значения переменной a. В данной lambda
    происходит генерация кубов модулей чисел в диапазоне от -a < -a+4 с последующим выводном в
    консоль. Присвоение происходит в дополнительных скобках к lambda, сама lambda тоже в них. Т.е. общая форма:
    (lambda a: <do smth with a>)(<this is a>). Решение by
    @Irina_I

    https://stepik.org/lesson/567071/step/7
    """
    (lambda a: print(*(abs(x) ** 3 for x in range(-a, -a + 4))))(int(input()))


# help(lambda_input)
# lambda_input()


def gen_lowercase():
    """
    Генерация последователности сочетаний букв из ascii_lowercase, с выводом четрех из них в консоль. На основании
    решения выше.

    """