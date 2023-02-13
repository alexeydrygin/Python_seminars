
import random
import os  # импортируем модуль os
os.system('clear')  # вызываем команду clear для очистки окна терминала.


candy_on_table = 120
max_candy_per_turn = 28


def human_turn():
    turn_candy = 0
    while True:
        turn_candy = int(input("Введите число конфет (1-28): "))
        if turn_candy > 0 and turn_candy <= max_candy_per_turn:
            return turn_candy
        else:
            print("Неверно. Введите число от 1 до 28")


def set_difficulty():
    difficulty = int(input("Выберите сложность противника (1-3): "))
    if difficulty < 1 or difficulty > 3:
        print("Неверно. Выберите сложность от 1 до 3")
        return set_difficulty()
    return difficulty


def bot_turn(difficulty):
    if difficulty == 1:
        turn_candy = max(1, (min(max_candy_per_turn, candy_on_table)))
    elif difficulty == 2:
        if candy_on_table >= max_candy_per_turn:
            turn_candy = max_candy_per_turn - 1
        else:
            turn_candy = candy_on_table - 1
    else:
        turn_candy = random.randint(
            1, min(max_candy_per_turn, candy_on_table)) if candy_on_table > 1 else 1
    print(f"Бот взял: {turn_candy} конфет.")
    return turn_candy


difficulty = set_difficulty()

while candy_on_table > 0:
    print("Конфет на столе:", candy_on_table)
    human_candy = human_turn()
    candy_on_table -= human_candy
    if candy_on_table <= 0:
        print("Вы выиграли!")
        break
    print("Конфет на столе:", candy_on_table)
    bot_candy = bot_turn(difficulty)
    candy_on_table -= bot_candy
    if candy_on_table <= 0:
        print("Бот выиграл!")
        break
