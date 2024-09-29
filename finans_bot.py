import telebot
from telebot import types

bot = telebot.TeleBot('6617225742:AAF5DtY2ohs-0n_GEQTnCit8dMSVofsHh5E')

# Словарь для хранения расходов пользователей
user_expenses = {}

# Словарь для хранения бюджетов пользователей
user_budgets = {}

# Словарь для хранения инвестиций пользователей
user_investments = {}

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Привет! Я бот для управления финансами. Используй /help для просмотра доступных команд.")

@bot.message_handler(commands=['help'])
def send_help(message):
    help_text = "/add_expense - Добавить расход\n/view_expenses - Просмотреть расходы\n/set_budget - Установить бюджет\n/add_investment - Добавить инвестицию\n/view_investments - Просмотреть инвестиции\n/financial_analysis - Анализ финансового положения"
    bot.reply_to(message, help_text)

@bot.message_handler(commands=['add_expense'])
def add_expense(message):
    # Разбиваем сообщение пользователя на категорию и сумму
    try:
        category, amount = message.text.split()[1:]
        amount = float(amount)
        if message.chat.id not in user_expenses:
            user_expenses[message.chat.id] = {}
        if category not in user_expenses[message.chat.id]:
            user_expenses[message.chat.id][category] = 0
        user_expenses[message.chat.id][category] += amount
        bot.reply_to(message, f"Расход {amount} добавлен в категорию {category}.")
    except ValueError:
        bot.reply_to(message, "Неверный формат. Используйте /add_expense <категория> <сумма>")

@bot.message_handler(commands=['view_expenses'])
def view_expenses(message):
    if message.chat.id in user_expenses:
        expenses_text = "Ваши расходы:\n"
        for category, amount in user_expenses[message.chat.id].items():
            expenses_text += f"{category}: {amount}\n"
        bot.reply_to(message, expenses_text)
    else:
        bot.reply_to(message, "У вас пока нет расходов.")

@bot.message_handler(commands=['set_budget'])
def set_budget(message):
    # Разбиваем сообщение пользователя на категорию и сумму бюджета
    try:
        category, budget = message.text.split()[1:]
        budget = float(budget)
        if message.chat.id not in user_budgets:
            user_budgets[message.chat.id] = {}
        user_budgets[message.chat.id][category] = budget
        bot.reply_to(message, f"Бюджет {budget} установлен для категории {category}.")
    except ValueError:
        bot.reply_to(message, "Неверный формат. Используйте /set_budget <категория> <сумма>")

@bot.message_handler(commands=['add_investment'])
def add_investment(message):
    # Разбиваем сообщение пользователя на категорию и сумму инвестиции
    try:
        category, amount = message.text.split()[1:]
        amount = float(amount)
        if message.chat.id not in user_investments:
            user_investments[message.chat.id] = {}
        if category not in user_investments[message.chat.id]:
            user_investments[message.chat.id][category] = 0
        user_investments[message.chat.id][category] += amount
        bot.reply_to(message, f"Инвестиция {amount} добавлена в категорию {category}.")
    except ValueError:
        bot.reply_to(message, "Неверный формат. Используйте /add_investment <категория> <сумма>")

@bot.message_handler(commands=['view_investments'])
def view_investments(message):
    if message.chat.id in user_investments:
        investments_text = "Ваши инвестиции:\n"
        for category, amount in user_investments[message.chat.id].items():
            investments_text += f"{category}: {amount}\n"
        bot.reply_to(message, investments_text)
    else:
        bot.reply_to(message, "У вас пока нет инвестиций.")

@bot.message_handler(commands=['financial_analysis'])
def financial_analysis(message):
    if message.chat.id in user_expenses and message.chat.id in user_investments:
        total_expenses = sum(user_expenses[message.chat.id].values())
        total_investments = sum(user_investments[message.chat.id].values())
        net_worth = total_investments - total_expenses
        analysis_text = f"Ваш общий расход: {total_expenses}\nВаши общие инвестиции: {total_investments}\nВаша чистая стоимость: {net_worth}"
        bot.reply_to(message, analysis_text)
    else:
        bot.reply_to(message, "Недостаточно данных для анализа.")

bot.polling()
