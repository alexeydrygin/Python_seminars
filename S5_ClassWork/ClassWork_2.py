# Напишите программу, удаляющую из текста все слова, содержащие "абв"
# Строка находится в файле.
# Пример: вапвап кеоррьл приветабв авпавп приветаб абв
# Вывод: вапвап кеоррьл авпавп приветаб

import os  # импортируем модуль os
os.system('clear')  # вызываем команду clear для очистки окна терминала.


# path = "ClassWork_2.txt"
# data = open(path, "r", encoding="utf-8")
# string = data.read()
# data.close()
# list_in = string.split()
# print(list_in)
# list_out = list(filter(lambda x: not "абв" in x, list_in))
# print(list_out)

with open("ClassWork_2.txt", "r", encoding="utf-8") as file:
    list = list(file.readline().split())
    print(list)
    stop_word = "абв"
    print("Стоп слово: ", stop_word)
    filterd_list = " ".join(filter(lambda x: not stop_word in x, list))
    print("Фильтр: ", filterd_list)
