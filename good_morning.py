import telebot

bot = telebot.TeleBot(
    "7363675903:AAGeH40Hf4mS_-JuW80DIvMjXUjlZypr3CI"
)  # ключ тетеграмм бота


# обработчик команды старт
@bot.message_handler(commands=["start"])
def start(message):
    bot.send_message(message.chat.id, "Hello World!")


# не отключать бот до ручного отключения
bot.polling(none_stop=True)
