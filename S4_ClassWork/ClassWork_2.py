# Найдите корни квадратного уравнения Ax ^ 2 + Bx + С = 0 двумя способами.

a = int(input("A = "))
b = int(input("B = "))
c = int(input("C = "))

d = b**2 - 4*a*c
if d > 0:
    x1 = (-b + d**0.5)/(2*a)
    x2 = (-b - d**0.5)/(2*a)
    print("x1 = ", x1)
    print("x2 = ", x2)
elif d == 0:
    x = -b/(2*a)
    print("x1 = x2 = ", x)
else:
    print("Корней нет")
