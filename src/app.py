import telebot
import base
from app_api import get_movie_info_by_name

bot = telebot.TeleBot(base.TOKEN)

print ("bot created")

@bot.message_handler(commands=["start"])
def start(message):
    bot.send_message(
        message.chat.id,
        "🎥 Welcome!\nUse /find_movie_by_name to search a movie"
    )

@bot.message_handler(commands=["find_movie_by_name"])
def ask_movie_name(message):
    bot.send_message(message.chat.id, "🎬 Enter the movie name:")
    bot.register_next_step_handler(message, send_movie_info)

def send_movie_info(message):
    if not message.text or message.text.startswith("/"):
        bot.send_message(message.chat.id, "❌ Please send only the movie name")
        return

    result = get_movie_info_by_name(message.text)

    bot.send_message(
        message.chat.id,
        result,
        parse_mode="Markdown"
    )

@bot.message_handler (commands=["menu"])
def send_message (message):
    markup = telebot.types.ReplyKeyboardMarkup()
    about_btn = telebot.types.KeyboardButton ("about")
    contact_us_btn = telebot.types.KeyboardButton ("contact us")
    back_to_home = telebot.types.KeyboardButton ("<")
    markup.add (about_btn, contact_us_btn, back_to_home)
    bot.send_message (message.chat.id, "select one option", reply_markup=markup)

@bot.message_handler (func=lambda messsage: True)
def send_message (message):
    if message.text == "contact us":
        name = "ilya kuti arab"
        github = "https://github.com/IlyaKuti"
        # info = {"my name is":name, "my Github link":github}
        info = (f"""my name is {name}
github link {github}""")
        bot.send_message (message.chat.id, info)
    elif message.text == "about":
        bot.send_message (message.chat.id, """👋 Hi! I’m Ilya Kooti Arab, the developer of this bot.
I made this bot to help you find movie information quickly and easily.""")
    elif message.text == "<":
        markup = telebot.types.ReplyKeyboardRemove()
        bot.send_message (message.chat.id, "Back to home", reply_markup=markup)
    else:
        bot.send_message (message.chat.id, "ERROR")

bot.infinity_polling()