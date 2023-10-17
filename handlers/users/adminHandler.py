from aiogram.types import Message
from aiogram.dispatcher.filters import Command
from keyboards.default.menuKeyvboard import menuKeyboard
from loader import bot, dp

from handlers.users.start import users

@dp.message_handler(Command('update'), state="*")
async def update_limit(msg: Message):
    if msg.from_user.id == 982935447:
        for k, v in users.items():
            v[1] = 0
        await msg.reply("Userslar limiti 0 ga tenglashtirildi.")
    else:
        await msg.reply('Siz bot admini emassiz!!!', reply_markup=menuKeyboard)

    
