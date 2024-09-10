import telebot
import get_weather
import readerjson

# ключ тетеграмм бота
bot = telebot.TeleBot(readerjson.parsjson("telegram_token"))


# # обработчик команды старт
@bot.message_handler(commands=["start"])
def start(message):
    bot.send_message(message.chat.id, get_weather.get_weather())


# # # не отключать бот до ручного отключения
bot.polling(none_stop=True)
