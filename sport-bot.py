import telebot
from telebot import types
import random

token = '--TOKEN--'
bot = telebot.TeleBot(token=token)

def hello_user(message):
    bot.send_message(message.chat.id,
                     f'/help -- Настройки' +
                     f'\n/nutrition -- Питание' +
                     f'\n/exercises -- Упражнения')
def eat(message):
    eat_list = [
        'Ешьте больше фруктов и овощей',
        'Пейте много воды',
        'Избегайте сладких напитков',
        'Употребляйте больше белка'
    ]
    bot.send_message(message.chat.id, eat_list[random.randint(0, len(eat_list)-1)])
# Расчитываем массу тела
def imt(message):
    """
    16 и меньше -- выраженный дефицит
    16-18.5 -- недостаточная масса
    18.5-25 -- норма
    25-30 --  избыточная масса
    30-35 --  ожирение первой степени
    35-40 --  ожирение второй степени
    40 и больше --  ожирение третьей степени
    """
    bot.send_message(message.chat.id, 'Скажи мне какой у тебя рост')

    @bot.message_handler(func=lambda message: True)
    def handle_rost(message):
        try:
            global rost
            rost = float(message.text)
            bot.send_message(message.chat.id, 'Скажи мне какой у тебя вес')
            bot.register_next_step_handler(message, handle_ves)
        except ValueError:
            bot.send_message(message.chat.id, 'Введи число')
            bot.register_next_step_handler(message, handle_rost)

    def handle_ves(message):
        try:
            ves = float(message.text)
            imt = ves / (rost / 100) ** 2
            if imt <= 16:
                bot.send_message(message.chat.id, 'У тебя выраженный дефицит массы тела')
            elif 16 < imt <= 18.5:
                bot.send_message(message.chat.id, 'У тебя недостаточная масса тела')
            elif 18.5 < imt <= 25:
                bot.send_message(message.chat.id, 'У тебя нормальная масса тела')
            elif 25 < imt <= 30:
                bot.send_message(message.chat.id, 'У тебя избыточная масса тела')
            elif 30 < imt <= 35:
                bot.send_message(message.chat.id, 'У тебя ожирение первой степени')
            elif 35 < imt <= 40:
                bot.send_message(message.chat.id, 'У тебя ожирение второй степени')
            else:
                bot.send_message(message.chat.id, 'У тебя ожирение третьей степени')
        except ValueError:
            bot.send_message(message.chat.id, 'Введи число')
            bot.register_next_step_handler(message, handle_ves)

@bot.message_handler(commands=['start', 'help'])
def handle_start(message):
    global current_language
    current_language = 'Russian'  # Default language
    bot.send_message(message.chat.id, 'Привет! Я спортивный бот. Я проконсультирую тебя по питанию и упражнениям.')
    hello_user(message)

# Питание
@bot.message_handler(commands=['nutrition'])
def handle_eat(message):
    bot.send_message(message.chat.id, 'Можешь использвать мои рекомендации по питанию')
    eat(message)
    bot.send_message(message.chat.id, 'Расчитаем ИМТ?' +  '\n я более точно подберу тебе питание, если буду знать твой ИМТ')
    bot.register_next_step_handler(message, imt_or_not)
def imt_or_not(message):
    if message.text == 'Да':
        imt(message)
    elif message.text == 'Нет':
        bot.send_message(message.chat.id, 'Хорошо, думаю тебе хватит моей рекомендации')
    else:
        bot.send_message(message.chat.id, 'Пожалуйста, ответь "да" или "нет"')

# Упражнения
@bot.message_handler(commands=['exercises'])
def exercises(message):
    bot.send_message(message.chat.id, 'Вот видео для старта занятий')
    video = open('videoplayback.mp4', 'rb')
    bot.send_video(message.chat.id, video, 'Это видео')

    bot.send_message(message.chat.id, 'Хотите посмотреть еще несколько видео? (да/нет)')
    bot.register_next_step_handler(message, more_exercises)
def more_exercises(message):
    if message.text.lower() == 'да':
        bot.send_video(message.chat.id, open('videoplayback.mp4', 'rb'))
        bot.send_video(message.chat.id, open('videoplayback.mp4', 'rb'))
    elif message.text.lower() == 'нет':
        bot.send_message(message.chat.id, 'Хорошо, до встречи!')
    else:
        bot.send_message(message.chat.id, 'Пожалуйста, ответьте "да" или "нет".')

@bot.message_handler(func=lambda message: True)
def handle_message(message):
    bot.reply_to(message, 'Пока что я не понимаю такую команду ' + message.text)
    bot.send_message(message.chat.id, 'Можешь выбрать из этих')
    hello_user(message)

bot.polling(non_stop=True)

