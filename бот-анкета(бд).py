from telebot import types, TeleBot
import sqlite3

bot = TeleBot('--TOKEN--')


@bot.message_handler(commands=['start'])
def start_handler(message):
    # Записываем в базу данных то что рассказал о себе пользователь
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()

    # Создаем таблицу, если она не существует
    cursor.execute('''
                CREATE TABLE IF NOT EXISTS users (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    user_id INTEGER,
                    gender TEXT,
                    age INTEGER,
                    city TEXT
                )
            ''')

    bot.send_message(message.chat.id, 'Привет! Я бот-опросник. Давай пройдем опрос для знакомства')
    bot.register_next_step_handler(message, start)
    bot.send_message(message.chat.id, 'Начнем знакомство?')
    conn.commit()
    conn.close()


def start(message):
    st = message.text
    if st == "Да":
        bot.send_message(message.chat.id, f'Раз вы сказали {st}, тогда давайте начнем!\n\n'
                                          f'Выберите действие:\n'
                                          f'/poll - Начать опрос')
    else:
        bot.send_message(message.chat.id, 'Жаль, что вы не хотите участвовать.')

# Хендлер для опроса пользователя
@bot.message_handler(commands=['poll'])
def poll_handler(message):
    bot.register_next_step_handler(message, polls)
    bot.send_message(message.chat.id, 'Начнем опрос?')

def polls(message):
    ps = message.text
    if ps == "Да":
        bot.send_message(message.chat.id, f'Раз вы сказали {ps}, тогда давайте начнем!')
        bot.send_message(message.chat.id, 'Ты Мужчина или Женщина(М\Ж)?')
        bot.register_next_step_handler(message, men_or_women)
    else:
        bot.send_message(message.chat.id, 'Жаль, что вы не хотите участвовать.')

def men_or_women(message):
    global mw
    mw = message.text
    bot.send_message(message.chat.id, f'Теперь я знаю, что ты {mw}')

    if mw == "М" or "Ж":
        bot.send_message(message.chat.id, 'Сколько тебе лет?')
    bot.register_next_step_handler(message, years_old)

def years_old(message):
    global yo
    yo = message.text
    bot.send_message(message.chat.id, f'Теперь я знаю, что тебе {yo} лет')
    if 11 <= int(yo) <= 18:  # Проверяем возраст в диапазоне 11-18
        bot.send_message(message.chat.id, 'Здравствуй, юный слушатель!')
    elif 19 <= int(yo) <= 40:  # Проверяем возраст в диапазоне 19-40
        bot.send_message(message.chat.id, 'Добрый день, молодой слушатель!')
    elif 41 <= int(yo) <= 60:  # Проверяем возраст в диапазоне 41-60
        bot.send_message(message.chat.id, 'Приветствую вас, наши взрослые друзья!')
    else:
        bot.send_message(message.chat.id,
                         'Прости, я не знаю, как тебя приветствовать.')  # Добавили обработку для других возрастов
    bot.send_message(message.chat.id, 'Расскажи мне от куда ты?')
    bot.register_next_step_handler(message, city_handler)

def city_handler(message):
    city = message.text
    bot.send_message(message.chat.id, f'Теперь я знаю, что ты из {city}, это прекрасный город!')

# Записываем в базу данных данные о пользователе
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    user_id = message.from_user.id
    gender = mw
    age = int(yo)

    cursor.execute("INSERT INTO users (user_id, gender, age, city) VALUES (?, ?, ?, ?)",
                   (user_id, gender, age, city))

    conn.commit()
    conn.close()

bot.polling()
