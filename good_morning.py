import sys
from aiogram import Bot
import asyncio
import readerjson
import text
import get_weather
import schedule    
import time    
bot = Bot(readerjson.parsjson("telegram_token"))
async def main():
    await bot.send_message(chat_id=text.chat_id_i, text=get_weather.get_weather_on_line())
    # await bot.send_message(chat_id=text.chat_id_n, text=get_weather.get_weather_on_line())
    sys.exit()



def job():
    print("hi")
        # if __name__ == "__main__":
        # asyncio.run(main())
schedule.every().day.at("21:40").do(job()) 

while True:
        schedule.run_pending()
        time.sleep(1)