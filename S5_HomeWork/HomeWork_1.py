# Создайте программу для игры с конфетами человек против бота.
# Условие задачи: На столе лежит 120 конфета.
# Играют два игрока делая ход друг после друга.
# Первый ход делает человек.
# За один ход можно забрать не более чем 28 конфет.
# Победитель - тот, кто оставил на столе 0 конфет.
# Сколько конфет нужно взять первому игроку,
# чтобы забрать все конфеты у своего конкурента?
#
# 2021 21 ---> 2000 бот4 -> 1996 .... бот --->29 --> 27 >> 2конф
#
# Добавьте игру против бота
# Подумайте как наделить бота ""интеллектом"" (Теория игр)



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


def bot_turn():
    turn_candy = max(1, (min(max_candy_per_turn, candy_on_table)))
    print(f"Бот взял: {turn_candy} конфет.")
    return turn_candy


while candy_on_table > 0:
    print("Конфет на столе:", candy_on_table)
    human_candy = human_turn()
    candy_on_table -= human_candy
    if candy_on_table <= 0:
        print("Вы выиграли!")
        break
    print("Конфет на столе:", candy_on_table)
    bot_candy = bot_turn()
    candy_on_table -= bot_candy
    if candy_on_table <= 0:
        print("Бот выиграл!")
        break