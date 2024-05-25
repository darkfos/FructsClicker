from aiogram.types.bot_command import BotCommand
from aiogram import Bot
from FructsClicker.bot.text.general import *


async def set_commands(bot: Bot):
    """
    Установка команд для бота
    :param bot:
    :return:
    """

    return await bot.set_my_commands(
        commands=[
            BotCommand(command="/start", description="Начало"),
            BotCommand(command="/help", description="Поддержка")
        ]
    )


async def set_descr_and_short_descr(bot: Bot) -> None:
    """
    Установка описание (короткого, обычного)
    :param bot:
    :return:
    """

    await bot.set_my_description(await txt_for_description())
    await bot.set_my_short_description(await short_descr_bot())


async def set_my_name(bot: Bot):
    """
    Установка имени бота
    :param bot:
    :return:
    """

    return await bot.set_my_name(name="Fructis")