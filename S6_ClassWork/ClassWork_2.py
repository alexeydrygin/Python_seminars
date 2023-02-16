# Дана последовательность чисел.
# Получить список уникальных элементов
# заданной последовательности.
#[1, 2, 3, 5, 1, 5, 3, 10] => [2, 10]
# *без использования count()


# from random import randrange

# quantity = 10
# list_1 = [randrange(10) for i in range(quantity)]
# print('Список: \n', list_1)

# list_2 = []
# for k in list_1:
#     b = 0
#     for g in list_1:
#         if k == g:
#             b += 1
#     if b == 1:
#         list_2.append(k)
# print('Уникальные элементы списка: \n', *list_2)

def find_unique(data):
    result = []
    results_new = []
    for el in data:
        if el not in result and el not in results_new:
            result.append(el)
            results_new.append(el)
        elif el in result:
            result.remove(el)
    print(results_new)
    return sorted(result)

sequence = [1, 1, 2, 2, 3, 10]
print(f'Исходная последовательность:\n {sequence}')
print(f'Результат:\n {find_unique(sequence)}')