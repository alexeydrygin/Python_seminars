# Создайте Бота для игры с конфетами человек против бота. (Дополнительно)

import random
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters


def start(update, context):
    context.user_data['candies'] = random.randint(10, 20)
    context.user_data['turn'] = 1
    context.bot.send_message(chat_id=update.effective_chat.id, text="Начинаем игру! В кучке {} конфет. Ваш ход.".format(context.user_data['candies']))


def candies(update, context):
    num_candies = int(update.message.text)
    if num_candies < 1 or num_candies > 3:
        context.bot.send_message(chat_id=update.effective_chat.id, text="Вы можете взять только от 1 до 3 конфет. Попробуйте еще раз.")
    else:
        context.user_data['candies'] -= num_candies
        if context.user_data['candies'] == 0:
            context.bot.send_message(chat_id=update.effective_chat.id, text="Поздравляем! Вы выиграли!")
        else:
            context.bot.send_message(chat_id=update.effective_chat.id, text="В кучке осталось {} конфет. Ход бота...".format(context.user_data['candies']))
            bot_take = random.randint(1, 3)
            context.user_data['candies'] -= bot_take
            if context.user_data['candies'] == 0:
                context.bot.send_message(chat_id=update.effective_chat.id, text="К сожалению, бот выиграл. Попробуйте еще раз.")
            else:
                context.bot.send_message(chat_id=update.effective_chat.id, text="Бот взял {} конфет. В кучке осталось {} конфет. Ваш ход.".format(bot_take, context.user_data['candies']))
                context.user_data['turn'] += 1


def main():
    updater = Updater('YOUR_TOKEN_HERE', use_context=True)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler('start', start))
    dp.add_handler(MessageHandler(Filters.text, candies))

    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()
