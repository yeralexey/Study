
import traceback  # https://docs.python.org/3/library/traceback.html?highlight=traceback#module-traceback
"""
Функция демонстрирует весь процесс преобразования данных методом .sort() и функцией sorted().
Если раскомментированы тестовый ввод и выводы данных и закомментирован ввод с клавиатуры
- виден процесс преобразования, сохраняет и выводит текст traceback.

https://stepik.org/lesson/567076/step/3

полный конспект темы:
https://github.com/yeralexey/Study/blob/master/notabene.py

"""
s = "-2 -1 8 11 4 5"                 # тестовый ввод
# s = input()                          # ввод с клавиатуры

lst = [int(i) for i in s.split()]       # генерация списка чисел
tp_lst = tuple(lst)                     # преобразование в кортеж

print(s)                 # введенные данные
print(lst)               # тестовый вывод до
print(tp_lst)            # тестовый вывод после

def sortanyway(array):
    try:
        array.sort()
        print("Сейчас был использован метод .sort")
        return array
    except AttributeError:
        print(f"сработало исключение, и будет использована функция sorted(). \nошибка:\n{traceback.format_exc()} ")
        t_lst = sorted(array)

        return t_lst

lst = sortanyway(lst)
print(lst)               # тестовый вывод после

tp_lst = tuple(sortanyway(tp_lst))
print(tp_lst)            # тестовый вывод после

# help(sorted_sort_exaple)
sorted_sort_exaple()