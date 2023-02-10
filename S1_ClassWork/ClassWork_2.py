# Напишите программу, которая принимает 5 чисел и находит максимальное из них

# array = [3, 4, 99, 23, 0]
# print(array)

# max = array[0]
# for num in array:
#     if num > max:
#         max = num

# print(f"max =", max)

INDEX = 5
nums = []
for num in range(0, INDEX):
    nums.append(int(input("Введите число:\n")))
print(f"Максимальное = {max(nums)}")
