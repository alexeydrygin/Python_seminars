# Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.
# 24
# 2 2 2 3

def prime_factors(n):
    i = 2
    factors = []
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
            factors.append(i)
    if n > 1:
        factors.append(n)
    return factors


N = int(input("Задайте число N: "))
print("Простые множители числа N: ", prime_factors(N))
