from aiogram.types import InlineKeyboardButton, WebAppInfo
from aiogram.utils.keyboard import InlineKeyboardBuilder

from src.configs.app import settings


def web_app_kb() -> InlineKeyboardBuilder:
    keyboard = InlineKeyboardBuilder()

    buttons = [
        InlineKeyboardButton(
            text="webapp", web_app=WebAppInfo(url=settings.WEBAPP_URL))]

    keyboard.row(*buttons, width=1)
    return keyboard.as_markup()
