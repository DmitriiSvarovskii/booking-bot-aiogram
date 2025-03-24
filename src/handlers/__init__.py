__all__ = ("router",)

from aiogram import Router

from src.handlers import start


router = Router(name=__name__)

router.include_routers(
    start.router,
)
