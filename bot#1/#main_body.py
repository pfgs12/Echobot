import asyncio
import logging
from aiogram import Dispatcher, types, Bot, Router
from aiogram.types import ReplyKeyboardRemove, ReplyKeyboardMarkup, KeyboardButton, Message
from aiogram.filters import CommandStart
from aiogram.filters.command import Command
from aiogram.fsm.storage.memory import MemoryStorage
dp = Dispatcher()
router = Router()
dp = Dispatcher(storage=MemoryStorage())
logging.basicConfig(level=logging.INFO)
bot = Bot(token = "YOUR TOKEN")
dp.include_router(router)
@router.message(Command("start"))
async def send_welcome(message: types.Message):
    kb = [
        [types.KeyboardButton(text='Сможешь повторить это?')],
        [types.KeyboardButton(text='А это?')]
        
    ]
    keyboard = types.ReplyKeyboardMarkup(keyboard=kb)
    await message.reply('Привет!Я эхо бот!', reply_markup=keyboard)
@router.message()
async def echo(message: types.Message):
    await message.answer(message.text)
async def main():
    await dp.start_polling(bot)
if __name__ == "__main__":
    asyncio.run(main())
