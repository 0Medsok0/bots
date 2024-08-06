import telebot
from telebot import types
import datetime
import time


bot = telebot.TeleBot('--TOKEN--')

@bot.message_handler(commands=['start'])
def send_welcome(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    itembtn1 = types.KeyboardButton('Запланировать встречу')
    markup.add(itembtn1)
    bot.send_message(message.chat.id, "Привет! Я бот для планирования встреч. Что ты хочешь сделать?", reply_markup=markup)

@bot.message_handler(func=lambda message: message.text == 'Запланировать встречу')
def schedule_meeting(message):
    bot.send_message(message.chat.id, "Введите дату и время встречи в формате 'ГГГГ-ММ-ДД ЧЧ:ММ' (например, 2023-12-25 15:00)")
    bot.register_next_step_handler(message, process_meeting_date)

def process_meeting_date(message):
    try:
        meeting_datetime = datetime.datetime.strptime(message.text, '%Y-%m-%d %H:%M')
        bot.send_message(message.chat.id, f"Встреча запланирована на {meeting_datetime.strftime('%Y-%m-%d %H:%M')}.")
        bot.send_message(message.chat.id, "Введите описание встречи:")
        bot.register_next_step_handler(message, process_meeting_description, meeting_datetime)
    except ValueError:
        bot.send_message(message.chat.id, "Неверный формат даты и времени. Пожалуйста, введите дату и время в формате 'ГГГГ-ММ-ДД ЧЧ:ММ'.")

def process_meeting_description(message, meeting_datetime):
    meeting_description = message.text
    bot.send_message(message.chat.id, f"Встреча '{meeting_description}' запланирована на {meeting_datetime.strftime('%Y-%m-%d %H:%M')}.")
    bot.send_message(message.chat.id, "Хотите установить напоминание?")
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    itembtn1 = types.KeyboardButton('Да')
    itembtn2 = types.KeyboardButton('Нет')
    markup.add(itembtn1, itembtn2)
    bot.register_next_step_handler(message, process_reminder, meeting_datetime, meeting_description)

def process_reminder(message, meeting_datetime, meeting_description):
    if message.text == 'Да':
        bot.send_message(message.chat.id, "Введите время напоминания (в минутах до встречи):")
        bot.register_next_step_handler(message, set_reminder, meeting_datetime, meeting_description)
    elif message.text == 'Нет':
        bot.send_message(message.chat.id, "Хорошо, напоминания не установлены.")
    else:
        bot.send_message(message.chat.id, "Неверный выбор.")

def set_reminder(message, meeting_datetime, meeting_description):
    try:
        reminder_minutes = int(message.text) # минуты напоминания
        reminder_datetime = meeting_datetime - datetime.timedelta(minutes=reminder_minutes) # дата и время напоминания
        bot.send_message(message.chat.id, f"Напоминание о встрече '{meeting_description}' установлено на {reminder_datetime.strftime('%Y-%m-%d %H:%M')}.")
        # Логика для отправки напоминания в нужное время ,задержка до времени напоминания
        time_to_wait = (reminder_datetime - datetime.datetime.now()).total_seconds()
        if time_to_wait > 0:
            time.sleep(time_to_wait)
            bot.send_message(message.chat.id,
                             f"Напоминание! Встреча '{meeting_description}' через {reminder_minutes} минут!")
    except ValueError:
        bot.send_message(message.chat.id, "Неверный формат времени. Пожалуйста, введите число.")

bot.polling()
