# Задайте список из вещественных чисел. Напишите программу,
# которая найдёт разницу между максимальным и минимальным значением дробной части элементов.

#    ```
#    Пример:
#    [1.1, 1.2, 3.1, 5, 10.01] => 0.19
#    ```

import os  # импортируем модуль os
os.system('clear')  # вызываем команду clear для очистки окна терминала.


def difference_of_min_and_max_fractional_parts(numbers):
    # Создаем переменные min_fractional_part и max_fractional_part со значениями 1 и 0 соответственно
    min_fractional_part = 1
    max_fractional_part = 0
    # Перебираем каждый элемент списка numbers
    for num in numbers:
        # Рассчитываем дробную часть числа
        fractional_part = num - int(num)
        # Сравниваем текущую дробную часть с минимальной и если текущая меньше, то обновляем минимальную
        if fractional_part < min_fractional_part:
            min_fractional_part = fractional_part
        # Сравниваем текущую дробную часть с максимальной и если текущая больше, то обновляем максимальную
        if fractional_part > max_fractional_part:
            max_fractional_part = fractional_part
    # Возвращаем разницу между максимальной и минимальной дробной частью
    return max_fractional_part - min_fractional_part


numbers = [1.1, 1.2, 3.1, 5, 10.01]
print(numbers)
print("Разница между максимальным и минимальным значением дробной части элементов:",
      difference_of_min_and_max_fractional_parts(numbers))
