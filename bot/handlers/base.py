#Other
from aiogram import Router
from aiogram.filters import CommandStart, Command
from aiogram.types import Message
#from aiogram.types.web_app_info import WebAppInfo

#Local
from FructsClicker.bot.keyboards.web_inl_kb import web_inl_kb


base_router: Router = Router()


@base_router.message(CommandStart())
async def start_command(message: Message) -> None:
    await message.answer(text="Отлично, вы готовы к игре?", reply_markup=await web_inl_kb())


@base_router.message(Command("help"))
async def help_command(message: Message) -> None:
    await message.answer(text="Помощь..")