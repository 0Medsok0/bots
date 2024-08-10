import telebot
import os

bot = telebot.TeleBot('--TOKEN--')

# Create a directory to store files
if not os.path.exists('files'):
    os.makedirs('files')

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, "Welcome! I can store and share files.\nUse /add to add a new file.\nUse /list to list all available files.\nUse /download [file_name] to download a file.")

@bot.message_handler(commands=['add'])
def add_file(message):
    bot.send_message(message.chat.id, "Please send me the file you want to add.")
    bot.register_next_step_handler(message, process_file)

def process_file(message):
    if message.document:
        file_info = bot.get_file(message.document.file_id)
        downloaded_file = bot.download_file(file_info.file_path)
        with open(f"files/{message.document.file_name}", 'wb') as new_file:
            new_file.write(downloaded_file)
        bot.send_message(message.chat.id, f"File {message.document.file_name} added successfully!")
    else:
        bot.send_message(message.chat.id, "Please send me a file.")

@bot.message_handler(commands=['list'])
def list_files(message):
    files = os.listdir('files')
    if files:
        file_list = "\n".join(files)
        bot.send_message(message.chat.id, f"Available files:\n{file_list}")
    else:
        bot.send_message(message.chat.id, "No files available.")

@bot.message_handler(commands=['download'])
def download_file(message):
    file_name = message.text.split()[1]
    if file_name in os.listdir('files'):
        with open(f"files/{file_name}", 'rb') as file:
            bot.send_document(message.chat.id, file)
    else:
        bot.send_message(message.chat.id, f"File {file_name} not found.")

bot.polling()
