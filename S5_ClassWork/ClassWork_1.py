# В файле находится N натуральных чисел.
# Среди чисел не хватает одного,
# чтобы выполнялось условие:
# A[i] - 1 = A[i - 1]
# Найдите это число.
# Пример: 1 2 3 4 6 7
# Вывод: 5

import os  # импортируем модуль os
os.system('clear')  # вызываем команду clear для очистки окна терминала.


path = "ClassWork_1.txt"
data = open(path, "r")
string = data.read()
data.close()
list = [int(i) for i in string.split()]
print(list)
for i in range(len(list) - 1):
    if list[i + 1] != list[i] + 1:
        print(list[i] + 1)
