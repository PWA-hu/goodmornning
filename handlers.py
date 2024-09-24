from aiogram import F, Router, types
from aiogram.filters import Command
from aiogram.types import Message
import get_weather
import keyboards
import text

router = Router()

# обработка  команды start
@router.message(Command("start"))
async def start_handler(msg: Message):
    await msg.answer(
        text.greet.format(name=msg.from_user.full_name), reply_markup=keyboards.menu
    )


@router.message(F.text == "Меню")
async def menu(msg: Message):
    await msg.answer(text.menu, reply_markup=keyboards.menu)

# обработка нажатия кнопки текущей погоды
@router.callback_query(F.data == "weather_online")
async def weather_online(clbck: types.CallbackQuery):
    await clbck.message.answer(get_weather.get_weather_on_line(), reply_markup=keyboards.menu)


# обработка нажатия кнопки текущей погоды
@router.callback_query(F.data == "weather_forecast")
async def weather_online(clbck: types.CallbackQuery):
    await clbck.message.answer(get_weather.get_weather_on_line(), reply_markup=keyboards.menu)