from aiogram import types
from aiogram.types import CallbackQuery

from aiogram.types import ChatActions

from aiogram.dispatcher.filters import Text

from states.photoState import PhotoState
from aiogram.dispatcher import FSMContext

from utils.photoraphy import photo_link
from utils.photolab import effect_picture

from loader import bot, dp
from keyboards.default.menuKeyvboard import menuKeyboard

from handlers.users.start import users


@dp.message_handler(Text("🎇 Effect"), state='*')
async def photo0(msg: types.Message, state: FSMContext):
    # await bot.delete_message(msg.from_user.id, msg.message_id-1)
    await msg.delete()
    msg_id = msg.from_user.id
    msg_name = msg.from_user.full_name
    if msg_id in users.keys():
        if users[msg_id][1] > 1:
            await msg.answer(
                f"Siz bugungi 2 ta limitdan foydalanib bo'ldingiz.\n\n"
                f"<b>Ertaga soat 00:00 dan boshlab sizga 2 ta yangi limit beriladi.</b>\n"
                f"<i>Iltimos ertaga harakat qilib ko'ring!!!</i>", reply_markup=menuKeyboard
            )
        else:
            album = types.MediaGroup()

            photo1 = "AgACAgQAAxkBAAEW-UNlK4Fg4bRVJzX6nSwz7byzzvUxDwAC3bExGyzcXVHFGcfpoFXG1wEAAwIAA3kAAzAE"
            photo2 = "AgACAgQAAxkBAAEW-ThlK3xRVS5ZwSXEP03cZp1AvS3iiwACfbIxG5JWXVEEpJ2lHl0vTgEAAwIAA3MAAzAE"
            photo3 = "AgACAgQAAxkBAAEW-UVlK4GpKAsKMwGIrStfMMPtkmAHlQACubIxG9jwXVHatEkZOcVjswEAAwIAA3kAAzAE"

            album.attach_photo(photo=photo1)
            album.attach_photo(photo=photo2)
            album.attach_photo(photo=photo3, caption="Siz ham o'z suratlaringizdan shunday effectlar yaratmoqchimisiz???\n"
                            f"<b>\nU holda menga o'z rasmingizni yuboring</b>"
                            f"\n\n<i>❗️Eslatib o'taman, Siz bir kunda faqat 2 ta rasmingizni tahrirlashingiz mumkin</i>")
            
            await msg.answer_media_group(media=album)
            await PhotoState.firstState.set()




@dp.message_handler(content_types='photo', state=PhotoState.firstState)
async def photo_handler(msg: types.Message, state: FSMContext):
    
    msg_id = msg.from_user.id
    msg_name = msg.from_user.full_name
    if msg_id in users.keys():
        if users[msg_id][1] > 1:
            await msg.answer(
                f"Siz bugungi 2 ta limitdan foydalanib bo'ldingiz.\n\n"
                f"<b>Ertaga soat 00:00 dan boshlab sizga 2 ta yangi limit beriladi.</b>\n"
                f"<i>Iltimos ertaga harakat qilib ko'ring!!!</i>", reply_markup=menuKeyboard
            )
            await state.finish()
        
        else:
            try:
                users[msg_id][1] += 1
                photo = msg.photo[-1]
                link = await photo_link(photo=photo)
                # await msg.answer(link)
                await bot.send_chat_action(chat_id=msg.chat.id, action=ChatActions.UPLOAD_PHOTO)
                qayta = await bot.send_message(chat_id=msg.chat.id, text='⏳ Rasm qayta ishlanmoqda')
                new_photo = await effect_picture(img_url=link)
                await qayta.delete()
                xabar = await bot.send_message(chat_id=msg.chat.id, text='Rasm Yuklanmoqda')
                for i in range(1,11):
                    text0 = i*10
                    text1 = i*"🟩"
                    text2 = (10-i)*"🟥"
                    await xabar.edit_text(f"{text0}%\n{text1}{text2}")
                await xabar.delete()
                await msg.reply_photo(photo=new_photo, caption="🤩 Effect berish muvaffaqqiyatli yakunlandi.", reply_markup=menuKeyboard)
                await state.finish()
            except:
                await msg.answer("Rasmingizda qandaydur kamchilik bor!!!\nIltimos boshqa rasm yuboring.", reply_markup=menuKeyboard)
                await qayta.delete()
                await PhotoState.firstState.set()



@dp.message_handler(Text("👨‍💻 Admin bilan bog'lanish"), state='*')
async def admin_contact(msg: types.Message):
    await msg.answer("Fikr va mulohazalaringizni adminga yozib qoldirishingiz mumkin.\n"
                     f"https://t.me/Asliddinbek_official", reply_markup=menuKeyboard)


dp.message_handler(content_types='text', state=PhotoState.firstState)
async def photo_handler_text(msg: types.Message, state: FSMContext):
    await msg.reply("Iltimos rasm yuboring!!!\nYoki botni qayta ishga tushiring\n👉 /start /start /start")
