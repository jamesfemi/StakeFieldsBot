import os
import telebot
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton

# Get the Bot Token from environment variables (we will set this on Render later)
BOT_TOKEN = os.environ.get('BOT_TOKEN')
bot = telebot.TeleBot(BOT_TOKEN)

# Function to attach the "Join Channel" button underneath any message
def get_channel_markup():
    markup = InlineKeyboardMarkup()
    # This creates the clickable button linking directly to your channel
    button = InlineKeyboardButton(text="Join sbgcasino channel now 🚀", url="https://t.me/sbgcasino")
    markup.add(button)
    return markup

# Handle the /start or /help commands
@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    welcome_text = (
        "👋 Welcome to the SentenceCounter Bot!\n\n"
        "Send me any block of text, and I will accurately count how many sentences are in it."
    )
    bot.reply_to(message, welcome_text, reply_markup=get_channel_markup())

# Handle normal text messages (This is where the counting happens)
@bot.message_handler(func=lambda message: True)
def count_sentences(message):
    text = message.text
    
    # A simple but effective sentence counter logic:
    # It splits text by periods, exclamation marks, and question marks
    raw_sentences = text.replace('!', '.').replace('?', '.').split('.')
    
    # Strip spaces and filter out completely empty entries
    sentences = [s.strip() for s in raw_sentences if s.strip()]
    count = len(sentences)
    
    response_text = f"📊 **Your text contains:** {count} sentence(s)."
    
    # Send the answer along with your channel button
    bot.reply_to(message, response_text, parse_mode="Markdown", reply_markup=get_channel_markup())

# Start the bot
if __name__ == "__main__":
    print("Bot is running...")
    bot.infinity_polling()
