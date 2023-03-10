# Задайте список. Напишите программу, которая определит, присутствует ли в заданном списке строк некое число.

# n = input("Введите число:\n")
# s = ["Hello", "dfsgsghedgh", "12", "uran39"]

# for element in s:
#     if n in element:
#         print(n, "входит в", element)
#     else:
#         print(n, "не входит в", element)

import os  # импортируем модуль os
os.system('clear')  # вызываем команду clear для очистки окна терминала.


def check_if_number_in_list(n, s):
    # Объявление функции с двумя аргументами: n и s, где n - искомое число, а s - список, в котором необходимо искать число n
    found = False
    # Объявление переменной found со значением False
    for element in s:
        # Цикл по элементам списка s
        if n in element:
            # Условие: если n является частью текущего элемента списка s
            print(f"{n} входит в {element}")
            # Вывод сообщения о том, что n входит в текущий элемент списка s
            found = True
            # Изменение значения переменной found на True
            break
            # Прерывание цикла
    if not found:
        # Условие: если переменная found имеет значение False
        print(f"{n} не входит в ни одном из элементов списка {s}")
        # Вывод сообщения о том, что n не входит в ни одном из элементов списка s


s = ["Hello", "dfsgsghedgh", "12", "uran39"]
print(s)
n = input("Введите число:\n")

check_if_number_in_list(n, s)
