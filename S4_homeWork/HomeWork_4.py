# ; Задана натуральная степень k.
# ; Сформировать случайным образом список коэффициентов (значения от 0 до 100)
# ; многочлена и записать в файл (или вывести в терминал) многочлен степени k.

import random

k = int(input("Введите натуральную степень k: "))
coefs = []
for i in range(k + 1):
    coefs.append(random.randint(0, 100))

 # Writing the polynomial to a file
with open("HomeWork_4_polynominal.txt", "w") as f:
    for i, coef in enumerate(coefs):
        if coef != 0:
            f.write("{}x^{}".format(coef, k - i))
        if i != k:
            f.write(" + ")
print("Многочлен записан в файл...")

# Printing the polynomial to the terminal
polynomial = ""
for i, coef in enumerate(coefs):
    if coef != 0:
        polynomial += "{}x^{}".format(coef, k - i)
        if i != k:
            polynomial += " + "
print(polynomial)
