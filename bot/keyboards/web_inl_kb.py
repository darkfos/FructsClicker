from aiogram.utils.keyboard import InlineKeyboardBuilder, InlineKeyboardButton
from aiogram.types.web_app_info import WebAppInfo


async def web_inl_kb() -> InlineKeyboardBuilder:

    kb = InlineKeyboardBuilder()
    kb.add(InlineKeyboardButton(
        text="Открыть",
        web_app=WebAppInfo(url="https://itproger.com")
    ))

    return kb.as_markup()