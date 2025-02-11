import asyncio
from aiogram import Bot, Dispatcher
from handlers import router
from aiogram.types import Message
from aiogram import  F
from yandexGPTdemo import AI
from config import TOKEN
bot = Bot(token=TOKEN, parse_mod='MarkdownV2')
dp = Dispatcher()



async def main():
    dp.include_router(router)
    await dp.start_polling(bot)

@router.message(F.text == 'anycomand')
async def send(message: Message, system, ID):
    text = AI(system)
    await bot.send_message(ID, text)


if __name__ == '__main__':
    asyncio.run(main())