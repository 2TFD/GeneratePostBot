from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.utils.keyboard import InlineKeyboardBuilder, ReplyKeyboardBuilder
import datebase as Pdb

startKb = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="каналы", callback_data='channel')],
    [InlineKeyboardButton(text="посты", callback_data='message')]
],)


post = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text='каналы')],
    [KeyboardButton(text='на главную')] 
], resize_keyboard=True)


channel = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text='добавление нового канала')],
    [KeyboardButton(text='добавление нового промта')],
    [KeyboardButton(text='удаление каналов')],
    [KeyboardButton(text='удаление промтов')],
    [KeyboardButton(text='мои каналы')],
    [KeyboardButton(text='мои промты')],
    [KeyboardButton(text='на главную')],
], resize_keyboard=True)


async def myKBchannels():
    channels = await Pdb.MyChannelDB()
    keyboard = ReplyKeyboardBuilder()
    for channel in channels:
        channel = str(channel[1])
        keyboard.add(KeyboardButton(text=channel))
    return keyboard.adjust(2).as_markup()

async def myKBpromts():
    promts = await Pdb.MyPromtlDB()
    keyboard = ReplyKeyboardBuilder()
    for promt in promts:
        promt = str(promt[0])
        keyboard.add(KeyboardButton(text=promt))
    return keyboard.adjust(2).as_markup()


async def myPromt():
    Promts = await Pdb.MyPromtlDB()
    keyboard = ReplyKeyboardBuilder()
    for promt in Promts:
        promt = str(promt[0])
        keyboard.add(KeyboardButton(text=promt))
    return keyboard.adjust(2).as_markup()

main = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text="на главную")]
], resize_keyboard=True)


