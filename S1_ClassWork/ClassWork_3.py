# Напишите программу, которая будет принимать на вход число N и выводить числа от - N до N
# 5 -> -5 -4 -3 -2 -1 0 1 2 3 4 5

# range(stop) -> range object range(start, stop[, step]) -> range object
# Return an object that produces a sequence of integers from start (inclusive) to stop (exclusive) by step. range(i, j) produces i, i+1, i+2, ..., j-1. start defaults to 0, and stop is omitted! range(4) produces 0, 1, 2, 3. These are exactly the valid indices for a list of 4 elements. When step is given, it specifies the increment ( or decrement).

# диапазон (остановка) -> объект диапазона диапазон (начало, остановка[, шаг]) -> объект диапазона
# Возвращает объект, который пошагово генерирует последовательность целых чисел от start (включительно) до stop (исключающий). диапазон(i, j) выдает i, i+1, i+2, ..., j-1. start по умолчанию равен 0, а stop опущен! диапазон(4) выдает 0, 1, 2, 3. Это точно допустимые индексы для списка из 4 элементов. Когда задан шаг, он указывает приращение (или декремент).

a = int(input("Введите число:\n"))
numbers = [i for i in range(-a, a + 1, 1)]
print(numbers)
