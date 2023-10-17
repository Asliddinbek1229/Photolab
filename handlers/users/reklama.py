from aiogram.types import Message, CallbackQuery
from aiogram.dispatcher import FSMContext

from states.adminState import AdminState
from keyboards.inline.reklamaKB import rek_kb

from handlers.users.start import users

from loader import dp, bot
import asyncio





@dp.message_handler(chat_id=982935447, commands=['reklama'])
async def reklama(msg: Message):
    await msg.answer(
        "Reklamani qaysi ko'rinishda yubormoqchisiz?", reply_markup=rek_kb
    )
    await AdminState.OneState.set()

@dp.callback_query_handler(text='text', state=AdminState.OneState)
async def send_text(call: CallbackQuery, state: FSMContext):
    await call.message.answer("Matn yuboring")
    await call.answer()
    await AdminState.textState.set()

@dp.message_handler(state=AdminState.textState)
async def send_matn(msg: Message, state: FSMContext):
    rek = msg.text
    users_1 = []
    for k, v in users.items():
        users_1.append(k)
    x = 0
    y = 0
    i = await msg.answer("✅ Reklama yuborilyapti, iltimos kutib turing...")
    for user in users_1:
        try:
            await bot.send_message(chat_id=user,
                                   text=rek)
            await asyncio.sleep(0.05)
            x += 1
        except:
            y += 1

    await i.delete()
    await msg.answer("<b>✅ Reklama yuborildi</b>\n\n"
                         f"Qabul qildi: {x} ta\n"
                         f"Yuborilmadi: {y} ta")
    await state.finish()

@dp.callback_query_handler(text='r_photo', state=AdminState.OneState)
async def get_photo(call: CallbackQuery, state: FSMContext):
    await call.message.answer("Rasm yuboring")
    await AdminState.photostate.set()

@dp.message_handler(content_types='photo', state=AdminState.photostate)
async def caption(msg: Message, state: FSMContext):
    photo = msg.photo[-1].file_id
    await state.update_data(
        {'photo_id':photo}
    )
    await msg.answer("Rasm uchun izoh yuboring")
    await AdminState.photostate2.set()


@dp.message_handler(state=AdminState.photostate2)
async def send_file(msg: Message, state: FSMContext):
    users_1 = []
    for k, v in users.items():
        users_1.append(k)
    caption = msg.text
    data = await state.get_data()
    photo = data.get('photo_id')
    x = 0
    y = 0
    i = await msg.answer("✅ Reklama yuborilyapti, iltimos kutib turing...")
    for user in users_1:
        try:
            await bot.send_photo(chat_id=user,
                                   photo=photo,
                                   caption=caption)
            await asyncio.sleep(0.05)
            x += 1
        except:
            y += 1

    await i.delete()
    await msg.answer("<b>✅ Reklama yuborildi</b>\n\n"
                         f"Qabul qildi: {x} ta\n"
                         f"Yuborilmadi: {y} ta")
    await state.finish()