#Other
from aiogram import Bot, Dispatcher
from aiogram.fsm.storage.memory import MemoryStorage
import logging, asyncio

#Local
from bot_settings import fruct_settings
from other.bot_sett_comm import set_commands, set_descr_and_short_descr, set_my_name
from handlers.base import base_router


async def start_bot():
    fruct_bot: Bot = Bot(token=fruct_settings.bot_token)
    storage: MemoryStorage = MemoryStorage()
    dp: Dispatcher = Dispatcher(bot=fruct_bot, storage=storage)

    #logging
    logging.basicConfig(level=logging.INFO)

    #settings
    await set_commands(bot=fruct_bot)
    await set_descr_and_short_descr(bot=fruct_bot)
    await set_my_name(bot=fruct_bot)

    #Include routers
    dp.include_routers(
        base_router
    )

    try:
        logging.info(msg="Бот начал свою работу")
        await dp.start_polling(fruct_bot)
    except Exception as ex:
        await dp.stop_polling()
        logging.critical(msg="Фруктовый замес окончился")


if __name__ == "__main__":
    asyncio.run(start_bot())