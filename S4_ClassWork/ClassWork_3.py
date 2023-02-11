# Задайте два числа.
# Напишите программу, которая найдет НОК
# (наименьшее общее кратное) этих двух чисел.
# НОК(а, б) = а*б/нод(а, б)

a = int(input("a = "))
b = int(input("b = "))


def gcd(a, b):
    while b:
        a, b = b, a % b
    return a


def lcm(a, b):
    return a * b // gcd(a, b)


def find_lcm(a, b):
    return lcm(a, b)


print(f"HOK = {find_lcm(a, b)}")
