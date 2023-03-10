# --Напишите программу, которая принимает на вход координаты двух точек и находит расстояние между ними в 2D пространстве.
# Пример:

# - A (3,6); B (2,1) -> 5,09
# - A (7,-5); B (1,-1) -> 7,21

def distance_2d(x1, y1, x2, y2):
    return round(((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5, 2)


# Example usage
x1 = float(input("Введите X1: "))
y1 = float(input("Введите Y1: "))
x2 = float(input("Введите X2: "))
y2 = float(input("Введите Y2: "))

dist = distance_2d(x1, y1, x2, y2)
print("Дистанция между двух точек:", dist)
