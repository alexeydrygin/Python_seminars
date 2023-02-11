# Напишите программу, в которой пользователь задает две строки,
# одна из них буква, а вторая слово или фраза.
# программа должна посчитать сколько раз буква из первой строки
# встретилась в слове или фразе из второй строки.
# (не используя встроенные функции)

def count_letter(letter, word):
    count = 0
    for char in word:
        if char == letter:
            count += 1
    return count


letter = input("Введите букву: ")
word = input("Введите слово или фразу: ")

result = count_letter(letter, word)
# print("Буква '{}' встретилась {} раз в '{}'.".format(letter, result, word))
print(f"Буква '{letter}' встретилась {result} раз в '{word}'.")
