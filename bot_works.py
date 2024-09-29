import telebot

bot = telebot.TeleBot('6617225742:AAF5DtY2ohs-0n_GEQTnCit8dMSVofsHh5E')

# Define a list of job listings
jobs = [
    {"title": "Software Engineer", "company": "TechCorp", "location": "San Francisco", "url": "https://example.com/job1"},
    {"title": "Data Scientist", "company": "DataScienceCo", "location": "New York", "url": "https://example.com/job2"},
    {"title": "Product Manager", "company": "ProductCo", "location": "Seattle", "url": "https://example.com/job3"},
]

# Handle the /start command
@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Welcome to the Job Search Bot! Here are some job listings for you:")
    display_jobs(message.chat.id)

# Handle the /search command
@bot.message_handler(commands=['search'])
def search_jobs(message):
    # Extract the user's input
    query = message.text.split('/search ', 1)[1]

    # Filter the job listings based on the user's input
    filtered_jobs = [job for job in jobs if query.lower() in job['title'].lower() or query.lower() in job['company'].lower()]

    # Display the filtered job listings to the user
    if filtered_jobs:
        for job in filtered_jobs:
            bot.send_message(message.chat.id, f"Job Title: {job['title']}\nCompany: {job['company']}\nLocation: {job['location']}\nURL: {job['url']}")
    else:
        bot.send_message(message.chat.id, "No jobs found for your query.")

# Function to display all job listings
def display_jobs(chat_id):
    for job in jobs:
        bot.send_message(chat_id, f"Job Title: {job['title']}\nCompany: {job['company']}\nLocation: {job['location']}\nURL: {job['url']}")

# Start the bot
bot.polling()
