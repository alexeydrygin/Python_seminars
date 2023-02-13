# Дан список чисел.
# Создайте спиок, в который попадают числа
# описываемые возрастающую последовательность.
# Порядок элементов менять нельзя.
# Например:
# [1, 5, 2, 3, 4, 6, 1, 7] = > [1, 2, 3] или[1, 7] или[1, 6, 7] и т.д.


from random import randint
import os  # импортируем модуль os
os.system('clear')  # вызываем команду clear для очистки окна терминала.

n = [17, 5, 3, 2, 8, 7, 6]
m = []
# max_num = max(n)
# t = randint(0, len(n) - 1)
# while n[t] == max_num:
#     t = randint(0, len(n) - 1)
# m.append(n[t])
# for i in range(t + 1, len(n)):
#     if n[i] > m[len(m) - 1]:
#         m.append(n[i])

for i in range(len(n) - 1):
    for j in range(i + 1, len(n)):
        if n[j] > n[i]:
            m.append(n[i])
            m.append(n[j])
            break
    if len(m) > 1:
        break

print(n)
print(m)
