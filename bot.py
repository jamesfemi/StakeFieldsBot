import os
import telebot
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton

# 1. Fetch the bot token from environment variables (Render will handle this safely)
BOT_TOKEN = os.environ.get('BOT_TOKEN')
bot = telebot.TeleBot(BOT_TOKEN)

# 2. Create the reusable channel button that goes under every message
def get_channel_markup():
    markup = InlineKeyboardMarkup()
    # Replace with your actual channel link or button text
    channel_button = InlineKeyboardButton(text="📢 Join Maths Tutor TG", url="https://t.me/mathstutortg")
    markup.add(channel_button)
    return markup

# 3. Handle the /start or /help commands
@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    welcome_text = (
        "👋 Welcome to the LetterCount Bot!\n\n"
        "Send me any word, sentence, or phrase, and I will instantly count the letters for you."
    )
    bot.reply_to(message, welcome_text, reply_markup=get_channel_markup())

# 4. Handle regular text messages (Count the letters!)
@bot.message_handler(func=lambda message: True)
def count_letters(message):
    user_text = message.text
    
    # Calculate counts
    total_chars_with_spaces = len(user_text)
    letters_only = len([char for char in user_text if char.isalpha()])
    
    response = (
        f"📊 **Your Text Results:**\n\n"
        f"🔤 **Letters only:** {letters_only}\n"
        f"📝 **Total characters (including spaces/symbols):** {total_chars_with_spaces}"
    )
    
    bot.reply_to(message, response, parse_mode='Markdown', reply_markup=get_channel_markup())

# 5. Start the bot
if __name__ == "__main__":
    print("Bot is running...")
    bot.infinity_polling()
