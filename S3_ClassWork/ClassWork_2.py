# Напишите программу, которая определит позицию второго вхождения строки в списке либо сообщит, что ее нет.
# Например:
# список: ["qwe", "asd", "zxc", "ertqwe"], ищем: "qwe" ответ: 3
# список: ["123", "234", "123", "567"], ищем: "123", ответ: -1

import os  # импортируем модуль os
os.system('clear')  # вызываем команду clear для очистки окна терминала.

##########################################################
# def find_second_occurrence(s, target):
#     count = 0
#     index = -1
#     for i, element in enumerate(s):
#         if element == target:
#             count += 1
#             if count == 2:
#                 index = i
#                 break
#     if index != -1:
#         return index
#     else:
#         return f"{target} не входит в список {s} дважды."

# # s = ["qwe", "asd", "zxc", "qwe"]
# s = ["123", "234", "123", "567"]
# print(s)
# target = input("введите вхождение:\n")
# print(
#     f"Позиция второго вхождения {target} в списке {s} расположена на {find_second_occurrence(s, target)} позиции")
##########################################################

# s = ["qwe", "asd", "zxc", "qwe"]
s = ["123", "234", "123", "567"]
find_s = input("Введите вхождение:\n")
# find_s = "qwe"
if s.count(find_s) < 2:
    print("Второго вхождения нет")
else:
    s.remove(find_s)  # удаляет первое вхождение
    print(f"Позиция второго вхождения: {s.index(find_s) + 1}")
