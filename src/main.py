import asyncio
import logging

from aiogram import Bot, Dispatcher
from aiogram.enums import ParseMode
from aiogram.client.default import DefaultBotProperties

from src.handlers import router
from src.configs.app import settings


logging.basicConfig(level=logging.INFO)

bot = Bot(token=settings.BOT_TOKEN)


async def main():
    try:
        bot = Bot(token=settings.BOT_TOKEN,
                  default=DefaultBotProperties(
                      parse_mode=ParseMode.HTML)
                  )

        dp = Dispatcher()
        dp.include_router(router=router)

        await bot.delete_webhook(drop_pending_updates=True)

        await dp.start_polling(bot)
    except Exception as e:
        print(f"Exception in main: {e}")

if __name__ == '__main__':
    try:
        asyncio.run(main())
    except Exception as e:
        print(e)
