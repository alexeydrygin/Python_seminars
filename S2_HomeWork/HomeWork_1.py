# Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.

# Эта программа вычисляет произведение чисел от 1 до N

# n = int(input("Введите число N: "))  # Запрашиваем число N

# # Основной цикл, который проходится по числам от 1 до N
# for i in range(1, n + 1):
#     # Вычисление произведения
#     result = 1
#     for j in range(1, i + 1):
#         result *= j
#     print(f"Произведение чисел до {i}: {result}")

import os  # импортируем модуль os
os.system('clear')  # вызываем команду clear для очистки окна терминала.

# считываем число N введенное пользователем и конвертируем его в целое число.
n = int(input("Введите число N: "))


# объявление функции find_multiplication с одним аргументом n.
def find_multiplication(n):
    result = []  # создаем пустой список result.
    multiplication = 1  # объявление переменной multiplication со значением 1.
    # цикл for, который проходится по всем числам от 1 до n+1.
    for i in range(1, n+1):
        # вычисляем произведение i и multiplication и записываем результат в multiplication.
        multiplication *= i
        # добавляем произведение в список result.
        result.append(multiplication)
    return result  # возвращаем список result из функции.


print(f"Пусть N = {n}, тогда {find_multiplication(n)}") # выводим результат выполнения функции find_multiplication в указанном формате.
