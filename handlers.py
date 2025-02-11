import asyncio
from aiogram import  F, Router, Bot
from aiogram.filters import CommandStart, Command
from aiogram.types import Message, CallbackQuery

import keyboard as kb
from aiogram.fsm.state import State, StatesGroup, default_state
from aiogram.fsm.context import FSMContext
import datebase as Pdb
router = Router()


class RegChannel(StatesGroup):
    id = State()
    name = State()


class RegPromt(StatesGroup):
    system = State()

class DelChannel(StatesGroup):
    delname = State()

class NewPost(StatesGroup):
    ID = State()
    promt_one = State()

class DelPromt(StatesGroup):
    delname = State()


@router.message(F.text == 'на главную')
async def start(message:Message):
    await message.answer(text="Это бот менеджер каналов \n выбери ниже нужный пункт \n 👇👇👇", reply_markup=kb.startKb)

@router.message(CommandStart())
async def start(message:Message):
    await message.answer(text="Это бот менеджер каналов \n выбери ниже нужный пункт \n 👇👇👇", reply_markup=kb.startKb)


@router.callback_query(F.data == 'channel')
async def kbChannel(callback:CallbackQuery):
    await callback.answer()
    await callback.message.answer(text='-', reply_markup=kb.channel)

@router.callback_query(F.data == 'message')
async def kbMessage(callback:CallbackQuery):
    await callback.answer()
    await callback.message.answer(text='-', reply_markup=kb.post)


@router.message(F.text == 'добавление нового канала')
async def newChannelID(message:Message, state: FSMContext):
    await state.set_state(RegChannel.id)
    await message.answer(text='введите id канала')

@router.message(RegChannel.id)
async def newChannelIDone(message:Message, state:FSMContext):
    await state.update_data(id=message.text)
    await state.set_state(RegChannel.name)
    await message.answer('введите имя канала')

@router.message(RegChannel.name)
async def newChannelIDtwo(message:Message, state:FSMContext):
    await state.update_data(name=message.text)
    data = await state.get_data()
    await message.answer(f'канал успешно добавлен\n id: {data["id"]}\n Имя: {data["name"]}')
    telegram_id = data["id"]
    username = data["name"]
    await Pdb.add_to_database_users(telegram_id, username)
    await state.clear()


@router.message(F.text == 'удаление каналов')
async def MyChannel(message:Message, state: FSMContext):
    await message.answer(text='👇', reply_markup=await kb.myKBchannels())
    await state.set_state(DelChannel.delname)
@router.message(DelChannel.delname)
async def delchannel(message:Message, state:FSMContext):
    await state.update_data(delname=message.text)
    data = await state.get_data()
    await Pdb.DelChannelDB(data['delname'])
    await state.clear()
    await message.answer(text='канал успешно удален', reply_markup=kb.startKb)



@router.message(F.text == 'удаление промтов')
async def Mypromtdel(message:Message, state: FSMContext):
    await message.answer(text='👇', reply_markup=await kb.myKBpromts())
    await state.set_state(DelPromt.delname)
@router.message(DelPromt.delname)
async def delPromt(message:Message, state:FSMContext):
    await state.update_data(delname=message.text)
    data = await state.get_data()
    await Pdb.DelPromtDB(data['delname'])
    await state.clear()
    await message.answer(text='промт успешно удален', reply_markup=kb.startKb)



@router.message(F.text == 'добавление нового промта')
async def newpromt(message:Message, state: FSMContext):
    await state.set_state(RegPromt.system)
    await message.answer(text='введите текст для system')

@router.message(RegPromt.system)
async def newpromtone(message:Message, state:FSMContext):
    await state.update_data(system=message.text)
    data = await state.get_data()
    await message.answer(f'промт успешно добавлен\n system: {data["system"]}')
    system = data["system"]
    await Pdb.add_to_database_promt(system)
    await state.clear()

@router.message(F.text == 'мои промты')
async def MyPromt(message:Message):
    promts = await Pdb.MyPromtlDB()
    for promt in promts:
        res = str(promt)
        await message.answer(res)

@router.message(F.text == 'мои каналы')
async def CheckChannel(message:Message):
    chennals = await Pdb.MyChannelDB()
    for chennal in chennals:
        res = str(chennal)
        await message.answer(res)

@router.message(F.text == 'каналы')
async def PostChannel(message:Message, state:FSMContext):
    await state.set_state(NewPost.ID)
    await message.answer(text='выберите канал👇', reply_markup=await kb.myKBchannels())

@router.message(NewPost.ID)
async def PostChannel_ID(message:Message, state:FSMContext):
    await state.update_data(ID = await Pdb.getIDDB(message.text))
    await state.set_state(NewPost.promt_one)
    await message.answer(text='выберите промт👇', reply_markup=await kb.myPromt())
@router.message(NewPost.promt_one)
async def PostChannel_promt1(message: Message, state:FSMContext):
    from run import send
    await state.update_data(promt_one=message.text)
    data = await state.get_data()
    await message.answer(f'готово\n id: {data["ID"]}\n promt: {data["promt_one"]}',reply_markup=kb.main)
    mess = message.text
    await send(message= mess,system=data["promt_one"], ID=data["ID"])
    await state.clear()

