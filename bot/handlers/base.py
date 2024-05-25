from aiogram import Router
from aiogram.filters import CommandStart, Command
from aiogram.types import Message


base_router: Router = Router()


@base_router.message(CommandStart())
async def start_command(message: Message) -> None:
    await message.answer(text="Привет! Ты у бота по фруктовому зажиму...")


@base_router.message(Command("help"))
async def help_command(message: Message) -> None:
    await message.answer(text="Помощь..")