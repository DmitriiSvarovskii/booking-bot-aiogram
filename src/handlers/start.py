import aiohttp
from aiogram import types, F, Router

from src.keyboards.start import web_app_kb
from src.configs.app import settings
from src.schemas.users import UserCreate

router = Router()

ENDPOINT_URL = settings.SERVICE_URL


@router.message(F.text == "/start")
async def start(message: types.Message):
    request_body = await create_user_request(message)
    print(request_body)
    data = await send_user_request(request_body)

    await message.answer(
        f"Ответ от сервиса: {data}\nНажми кнопку ниже, чтобы открыть WebApp:",
        reply_markup=web_app_kb()
    )


async def create_user_request(message: types.Message) -> dict:
    return UserCreate(
        telegram_id=message.from_user.id,
        first_name=message.from_user.first_name or None,
        last_name=message.from_user.last_name or None,
        username=message.from_user.username or None,
        is_premium=message.from_user.is_premium or False
    ).model_dump(exclude_none=True)


async def send_user_request(request_body: dict) -> dict:
    async with aiohttp.ClientSession() as session:
        async with session.post(
            f"{ENDPOINT_URL}/user/",
            json=request_body
        ) as response:
            if response.status == 201:
                return await response.json()
            else:
                return {"error": f"Ошибка {response.status}"}
