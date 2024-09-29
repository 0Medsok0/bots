import telebot
from telebot import types
import random

bot = telebot.TeleBot('YOUR_TELEGRAM_BOT_TOKEN')

# Словарь для хранения слов на изучение
vocabulary = {
    "apple": "яблоко",
    "banana": "банан",
    "cat": "кот",
    "dog": "собака",
    "house": "дом"
}

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Привет! Я бот для изучения языков. Используй /help для просмотра доступных команд.")

@bot.message_handler(commands=['help'])
def send_help(message):
    help_text = "/learn_words - Изучить слова\n/take_test - Пройти тест\n/play_game - Игра для запоминания слов\n/add_word - Добавить новое слово"
    bot.reply_to(message, help_text)

@bot.message_handler(commands=['learn_words'])
def learn_words(message):
    words_text = "Слова на изучение:\n"
    for word, translation in vocabulary.items():
        words_text += f"{word} - {translation}\n"
    bot.reply_to(message, words_text)

@bot.message_handler(commands=['take_test'])
def take_test(message):
    score = 0
    words = list(vocabulary.keys())
    random.shuffle(words)
    for word in words:
        translation = vocabulary[word]
        options = [translation] + random.sample(list(vocabulary.values()), 3)
        random.shuffle(options)
        markup = types.ReplyKeyboardMarkup(one_time_keyboard=True)
        for option in options:
            markup.add(types.KeyboardButton(option))
        bot.send_message(message.chat.id, f"Выберите перевод слова '{word}':", reply_markup=markup)
        user_answer = bot.wait_for_message(message.chat.id).text
        if user_answer == translation:
            score += 1
    bot.send_message(message.chat.id, f"Ваш результат: {score}/{len(vocabulary)}")

@bot.message_handler(commands=['play_game'])
def play_game(message):
    words = list(vocabulary.keys())
    random.shuffle(words)
    correct_answers = 0
    for word in words:
        translation = vocabulary[word]
        options = [translation] + random.sample(list(vocabulary.values()), 3)
        random.shuffle(options)
        markup = types.ReplyKeyboardMarkup(one_time_keyboard=True)
        for option in options:
            markup.add(types.KeyboardButton(option))
        bot.send_message(message.chat.id, f"Выберите перевод слова '{word}':", reply_markup=markup)
        user_answer = bot.wait_for_message(message.chat.id).text
        if user_answer == translation:
            correct_answers += 1
    bot.send_message(message.chat.id, f"Ваш результат: {correct_answers}/{len(vocabulary)}")

@bot.message_handler(commands=['add_word'])
def add_word(message):
    try:
        word, translation = message.text.split()[1:]
        vocabulary[word] = translation
        bot.reply_to(message, f"Слово '{word}' добавлено в словарь.")
    except ValueError:
        bot.reply_to(message, "Неверный формат. Используйте /add_word <слово> <перевод>")

bot.polling()
