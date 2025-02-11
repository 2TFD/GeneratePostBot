import aiosqlite
import asyncio

async def add_to_database_users(telegram_id, username):
    async with aiosqlite.connect('tg.db') as db:
        await db.execute("CREATE TABLE IF NOT EXISTS users (telegram_id BIGINT, username TEXT)")
        await db.execute("INSERT INTO users (telegram_id, username) VALUES(?, ?)",
                         (telegram_id, username))
        await db.commit()


async def add_to_database_promt(system):
    async with aiosqlite.connect('promt.db') as db:
        await db.execute("CREATE TABLE IF NOT EXISTS promt (system TEXT)")
        await db.execute("INSERT INTO promt (system) VALUES(?)",
                         (system,))
        await db.commit()



async def MyChannelDB():
    async with aiosqlite.connect('tg.db') as db:
        async with db.execute('SELECT * FROM users') as cursor:
            channels = await cursor.fetchall()
        return channels

async def MyPromtlDB():
    async with aiosqlite.connect('promt.db') as db:
        async with db.execute('SELECT * FROM promt') as cursor:
            promts = await cursor.fetchall()
        return promts


async def DelChannelDB(name):
    async with aiosqlite.connect('tg.db') as db:
        async with db.execute(f'DELETE FROM users WHERE username= ?',(name,)):
            await db.commit()
            print('успешно удалено')

async def DelPromtDB(name):
    async with aiosqlite.connect('promt.db') as db:
        async with db.execute(f'DELETE FROM promt WHERE system= ?',(name,)):
            await db.commit()
            print('успешно удалено')


async def getIDDB(name):
    async with aiosqlite.connect('tg.db') as db:
        async with db.execute(f'SELECT telegram_id FROM users WHERE username= ?',(name,)) as cursor:
            ID = await cursor.fetchall()
            return ID[0][0]

