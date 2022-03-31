from main import bot, dp

from aiogram.types import Message
from config import my_id

async def send_to_admin(dp):
    await bot.send_message(chat_id=my_id, text = "Hi, hala-la hay!")