from dotenv import load_dotenv
import os
import telebot

load_dotenv()
TOKEN = os.getenv('BOT_TOKEN')

if not TOKEN:
    print("No BOT_TOKEN found. Please add it to the .env file.")
    exit(1)

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Hello! Your bot is running.")

@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.reply_to(message, f"You said: {message.text}")

print("Bot is running...")
bot.polling()
