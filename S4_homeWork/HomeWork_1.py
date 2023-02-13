# Вычислить число Pi c заданной точностью d, не используя ф. round()
# Пример:
# при $d = 0.001, π = 3.141.$ $10^{-1} ≤ d ≤10^{-10}$

# -------------------------не разобрался((()))--------------------------------

# def calc_pi(d):
#     pi = 3.14159265358979323846
#     pi_string = str(pi)
#     for i, char in enumerate(pi_string):
#         if char == ".":
#             index = i + 1
#             break
#     return float(pi_string[:index + int(d * 10) + 1])
# d = float(input("Enter the desired precision (e.g. 0.001):\n"))
# print(f"The value of Pi is: {calc_pi(d)}")


# # Initialize denominator
# k = 1
# # Initialize sum
# s = 0
# for i in range(10000000000):
#     # even index elements are positive
#     if i % 2 == 0:
#         s += 4 / k
#     else:
#         # odd index elements are negative
#         s -= 4 / k
#     # denominator is odd
#     k += 2
# print(s)


# def calc_pi(d):
#     # Initialize denominator
#     k = 1
#     # Initialize sum
#     s = 0
#     for i in range(int(1 / d)):
#         # even index elements are positive
#         if i % 2 == 0:
#             s += 4 / k
#         else:
#             # odd index elements are negative
#             s -= 4 / k
#         # denominator is odd
#         k += 2
#     return s


# d = float(input("Задайте точность вычисления (0,001):\n"))
# print(f"Число π = {calc_pi(d)}")

from math import pi

num = int(input("Введите число знаков после запятой: "))
stroka = str(pi)
print("π = ", float(stroka[:num+2]))
