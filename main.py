from aiogram import Bot, Dispatcher
from aiogram.fsm.storage.memory import MemoryStorage
import readerjson
from handlers import router
import asyncio
import logging


async def main():
    bot = Bot(token=readerjson.parsjson("telegram_token"))
    dp = Dispatcher(storage=MemoryStorage())
    dp.include_router(router)
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot, allowed_updates=dp.resolve_used_update_types())


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())
