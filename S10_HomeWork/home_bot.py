from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from fractions import Fraction
import logging

# Включить ведение журнала
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

logger = logging.getLogger(__name__)

# Определите функции обратного вызова для команд бота
def start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id,
                             text='Привет! Я бот-калькулятор. Вы можете использовать меня для выполнения основных арифметических операций с рациональными числами. Чтобы использовать me, просто введите математическое выражение.')

def help(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id,
                             text='Вы можете использовать меня для выполнения основных арифметических операций с рациональными числами. Чтобы использовать me, просто введите математическое выражение с операторами +, -, * или / между двумя числами. Например: "1/2 + 3/4"')

def calculate(update, context):
    try:
        # Извлеките пользовательский ввод
        expression = update.message.text
        
        # Преобразуйте выражение в список операндов и операторов
        operands = [Fraction(x) for x in expression.split(' ') if '/' in x]
        operators = [x for x in expression.split(' ') if x in ['+', '-', '*', '/']]
        
        # Вычисление
        result = operands[0]
        for i in range(len(operators)):
            if operators[i] == '+':
                result += operands[i+1]
            elif operators[i] == '-':
                result -= operands[i+1]
            elif operators[i] == '*':
                result *= operands[i+1]
            elif operators[i] == '/':
                result /= operands[i+1]
                
        # Отправьте результат пользователю и зарегистрируйте ввод и результат
        context.bot.send_message(chat_id=update.effective_chat.id,
                                 text=str(result))
        logger.info(f"Пользователь {update.effective_user.id} ввел: {expression}. Результат: {str(result)}")
    except Exception as e:
        # Обрабатывать любые ошибки, возникающие во время вычисления
        logger.error(str(e))
        context.bot.send_message(chat_id=update.effective_chat.id,
                                 text='Извините, я не смог выполнить расчет. Пожалуйста, введите допустимое математическое выражение.')

# Настройте бота с необходимыми обработчиками и начните опрос сообщений
def main():
    # Вставьте свой токен бота здесь
    TOKEN = '5976766519:AAE-F_WQoDdZ-Eu4qbZ7c4DXgR7YxLHe5Zk'

    updater = Updater(TOKEN, use_context=True)
    dispatcher = updater.dispatcher

    # Определите обработчики команд и сообщений
    start_handler = CommandHandler('start', start)
    help_handler = CommandHandler('help', help)
    message_handler = MessageHandler(Filters.text & (~Filters.command), calculate)

    # Добавьте обработчики в диспетчер
    dispatcher.add_handler(start_handler)
    dispatcher.add_handler(help_handler)
    dispatcher.add_handler(message_handler)

    # Запустите бота
    updater.start_polling()
    logger.info('Бот запущен')
    updater.idle()

if __name__ == '__main__':
    main()
