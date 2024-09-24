# import schedule    
# import time    
# def job():    
#     print("I'm working...")   


# schedule.every().day.at("21:58").do(job) 



# while True:
#     schedule.run_pending()
#     time.sleep(1)
import sys
from aiogram import Bot
import asyncio
import readerjson
import text
import get_weather
import schedule    
import time    

import schedule    
import time    
def job():    
    bot = Bot(readerjson.parsjson("telegram_token"))
    async def main():
        await bot.send_message(chat_id=text.chat_id_n, text=get_weather.get_weather_on_line())
        print ("hi")
    if __name__ == "__main__":
        asyncio.run(main()) 
    # await bot.send_message(chat_id=text.chat_id_n, text=get_weather.get_weather_on_line())
        # sys.exit()


schedule.every().day.at("07:00").do(job) 



while True:
    schedule.run_pending()
    time.sleep(1)


