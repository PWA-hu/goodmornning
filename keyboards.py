from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, KeyboardButton, ReplyKeyboardMarkup, ReplyKeyboardRemove
# кнопки меню
menu = [
    [InlineKeyboardButton(text="текущая погода", callback_data="weather_online"),
    InlineKeyboardButton(text="Прогноз погоды", callback_data="weather_forecast")]

]
menu = InlineKeyboardMarkup(inline_keyboard=menu)

# exit_kb = ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text="◀️ Выйти в меню")]], resize_keyboard=True)
# iexit_kb = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text="◀️ Выйти в меню", callback_data="menu")]])