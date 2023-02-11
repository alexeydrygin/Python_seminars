# Напишите программу, которая будет принимать дробь и показывать первую цифру дробной части числа

def first_digit_of_fractional_part(num):
    # Получаем строковое представление дробной части числа
    fractional_part = str(num).split('.')[1]
    # Возвращаем первую цифру дробной части
    return int(fractional_part[0])


num = float(input("Введите десятичную дробь:\n"))

print("Первой цифрой десятичной дроби", num,
      "является", first_digit_of_fractional_part(num))
