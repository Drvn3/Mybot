import os
import telebot
from dotenv import load_dotenv

load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN")
bot = telebot.TeleBot(BOT_TOKEN)

@bot.message_handler(commands=['start'])
def start(msg):
    bot.reply_to(msg, "Welcome to Hot🔥 News bot! Your free 24-hour trial has started. Use /news to get the latest summaries.")

@bot.message_handler(commands=['news'])
def news(msg):
    bot.reply_to(msg, "Fetching latest news... (demo mode)")

bot.infinity_polling()
