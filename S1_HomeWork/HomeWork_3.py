# --Напишите программу, которая принимает на вход координаты точки (X и Y), причём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти плоскости,
# в которой находится эта точка (или на какой оси она находится).
# Пример:

# - x=34; y=-30 -> 4
# - x=2; y=4-> 1
# - x=-34; y=-30 -> 3

def determine_quarter(x, y):
    if x > 0 and y > 0:
        return 1
    elif x < 0 and y > 0:
        return 2
    elif x < 0 and y < 0:
        return 3
    elif x > 0 and y < 0:
        return 4
    elif x == 0:
        return "on the X axis"
    elif y == 0:
        return "on the Y axis"


x = int(input("Введите значение X: "))
y = int(input("Введите значение Y: "))

result = determine_quarter(x, y)
print("Точка находится в четверти:", result)
