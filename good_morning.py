
import telebot
import get_weather
import readerjson

# ключ тетеграмм бота
bot = telebot.TeleBot(readerjson.parsjson("telegram_token"))


# обработчик команды старт
@bot.message_handler(commands=["start"])
def start(message):
    bot.send_message(message.chat.id, get_weather.get_weather())


# не отключать бот до ручного отключения
bot.polling(none_stop=True)
import telebot
import get_weather
import readerjson
from telebot import types 
# ключ тетеграмм бота
bot = telebot.TeleBot(readerjson.parsjson("telegram_token"))
@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn_real_time_weather = types.KeyboardButton("Какая сейчас погода❓")
    # btn_weather_forecast = types.KeyboardButton("Прогноз погоды")
    markup.add(btn_real_time_weather)
    bot.send_message(message.chat.id, text="Привет, {0.first_name}! Я твой мини бот".format(message.from_user), reply_markup=markup)



@bot.message_handler(commands=['begin'])
def begin(message):
    client_id = message.from_user.id
    bot.send_message(chat_id=client_id, text='Enter data: ')






@bot.message_handler(content_types=['text'])
def func(message):
    
    if(message.text == "Какая сейчас погода❓"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        bot.send_message(message.chat.id, text="В каком городе помотреть погоду❓")
        # bot.send_message(message.chat.id, get_weather.get_weather_on_line())
        btn_real_time_weather = types.KeyboardButton("Какая сейчас погода❓")
        markup.add(btn_real_time_weather)
    else:
         bot.send_message(message.chat.id, text="неизвестная команда")


# def btn():
#     markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
#     btn_real_time_weather = types.Kimport telebot
import get_weather
import readerjson
from telebot import types 
# ключ тетеграмм бота
bot = telebot.TeleBot(readerjson.parsjson("telegram_token"))
@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn_real_time_weather = types.KeyboardButton("Какая сейчас погода❓")
    # btn_weather_forecast = types.KeyboardButton("Прогноз погоды")
    markup.add(btn_real_time_weather)
    bot.send_message(message.chat.id, text="Привет, {0.first_name}! Я твой мини бот".format(message.from_user), reply_markup=markup)



@bot.message_handler(commands=['begin'])
def begin(message):
    client_id = message.from_user.id
    bot.send_message(chat_id=client_id, text='Enter data: ')






@bot.message_handler(content_types=['text'])
def func(message):
    
    if(message.text == "Какая сейчас погода❓"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        bot.send_message(message.chat.id, text="В каком городе помотреть погоду❓")
        # bot.send_message(message.chat.id, get_weather.get_weather_on_line())
        btn_real_time_weather = types.KeyboardButton("Какая сейчас погода❓")
        markup.add(btn_real_time_weather)
    else:
         bot.send_message(message.chat.id, text="неизвестная команда")


# def btn():
#     markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
#     btn_real_time_weather = types.KeyboardButton("Какая сейчас погода❓")
#     btn_real_time_weather = types.KeyboardButton("Прогноз погоды")
#     markup.add(btn_real_time_weather)
#     bot.send_message(message.chat.id, text="Привет, {0.first_name}! Я твой мини бот".format(message.from_user), reply_markup=markup)
#     return 




# # # обработчик команды старт
# @bot.message_handler(commands=["start"])
# def start(message):
#     bot.send_message(message.chat.id, get_weather.get_weather())


# # # # не отключать бот до ручного отключения
bot.polling(none_stop=True)
eyboardButton("Какая сейчас погода❓")
#     btn_real_time_weather = types.KeyboardButton("Прогноз погоды")
#     markup.add(btn_real_time_weather)
#     bot.send_message(message.chat.id, text="Привет, {0.first_name}! Я твой мини бот".format(message.from_user), reply_markup=markup)
#     return 




# # # обработчик команды старт
# @bot.message_handler(commands=["start"])
# def start(message):
#     bot.send_message(message.chat.id, get_weather.get_weather())


# # # # не отключать бот до ручного отключения
bot.polling(none_stop=True)
