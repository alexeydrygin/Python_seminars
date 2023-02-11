# Напишите программу, которая будет преобразовывать десятичное число в двоичное.

#    ```
#    Пример:
#    45 -> 101101
#    3 -> 11
#    2 -> 10
#    ```

import os  # импортируем модуль os
os.system('clear')  # вызываем команду clear для очистки окна терминала.


# Объявление функции decimal_to_binary, которая принимает аргумент decimal
def decimal_to_binary(decimal):
    # Инициализация пустой строки binary, куда будет записываться двоичное представление
    binary = ""
    # Цикл while, который выполняется, пока decimal больше нуля
    while decimal > 0:
        # Добавление в строку binary остатка от деления decimal на 2 в виде строки
        binary = str(decimal % 2) + binary
        # Округление вниз значения decimal путем деления на 2 без остатка
        decimal = decimal // 2
    # Возврат результата в виде двоичной строки
    return binary


decimal = int(input("Введите десятичное число:\n"))

print(f"Число {decimal} в двоичном представлении:", decimal_to_binary(decimal))
