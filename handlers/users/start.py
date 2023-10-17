from aiogram import types
from aiogram.dispatcher.filters import Command

from keyboards.inline.subscription import chek_button
from utils.misc.subscription import check
from data.config import CHANNELS, ADMINS



from loader import dp, bot

from keyboards.default.menuKeyvboard import menuKeyboard

users = {982935447: ['Asliddin 🇪🇭', 2],
         5118894186: ['Kompyuter xizmatlari', 1],
         1339330585: ['SADULLOH', 2],
         6399246532: ['💞💞', 2],
         855997578: ['Nodiraxon Bozorboyevna😊🙂 Axmadaliyeva', 0],
         569719079: ['С. Б. Ахмедова 22', 0],
         5357920886: ['•™•', 2],
         5102556968: ['Sohib Kuvayev', 2],
         5997942326: ['Abdumuxtor', 0],
         818234562: ['™TM™', 2],
         5728922975: ['Sh....', 2],
         1429936437: ['Samandar', 2],
         2121270055: ['⚜️HUMOYUN⚜️', 0],
         1483757455: ['Мунира Курбонова', 0],
         6199861108: ['Qalandarova Dilrabo', 2],
         493981667: ['𝓓𝓲𝓵𝓼𝓱𝓸𝓭𝓫𝓮𝓴 𝓨𝓪𝓺𝓾𝓫𝓫𝓸𝔂𝓮𝓿', 1],
         5761631472: ['@Eldor_Raxmonov', 2],
         2062270180: ['☝️МashaAlloh👆', 2],
         5985068114: ['꧁H҉A҉C҉K҉E҉R҉꧂', 2],
         307959200: ['Shokirjon Yulchibayev', 1],
         2122164437: ['꯭➊⃘⃝꯭➣⃘⃝꯭🕋𝚳꯭꯭𝚰꯭꯭𝐑𝐉꯭꯭𝚨꯭꯭𝐋꯭꯭𝚯꯭꯭𝐋꯭꯭➤⃝⃚⃖❤️', 1],
         972609448: ['Zuhriddin', 1],
         6674571198: ['Isfandiyor Xolbekov', 0]
         }

@dp.message_handler(Command('start'), state='*')
async def show_channels(message: types.Message):
    user_name = message.from_user.full_name
    user_id = message.from_user.id
    if user_id in users.keys():
        await bot.send_message(
            chat_id=982935447, text=f"{user_name} foydalanuvchi botga qayta start bosdi."
            f"\nBazadagi foydalanuvchilar soni {len(users)}\n{users}"
        )
    else:
        limit = 0
        users[user_id] = [user_name, limit]
        await bot.send_message(
            chat_id=982935447, text=f"Bazada yangi foydalanuvchi bor.\
                \nName: <b>{user_name}</b>\
                \nBazadagi foydalanuvchilar soni {len(users)}\n{users} "
        )
    
    subscription = int()
    for channel in CHANNELS:
        status = await check(user_id=message.from_user.id, channel=channel)
        channel = await bot.get_chat(channel)
        if status:
            subscription += 1

    if subscription == 1:
        await message.answer(
            f"Assalomu alaykum <b>{message.from_user.full_name}</b>\n"
            "<b>Quyidagi bo'limlardan birini tanlang 👇👇👇</b>", reply_markup=menuKeyboard
        )
    else:
        await message.answer(f"Quyidagi kanallarga obuna bo'ling: 👇",
                        reply_markup=chek_button,
                        disable_web_page_preview=True)


@dp.callback_query_handler(text="check_subs")
async def checker(call: types.CallbackQuery):
    # await call.answer()
    subscription = int()
    for channel in CHANNELS:
        status = await check(user_id=call.from_user.id, channel=channel)
        channel = await bot.get_chat(channel)
        if status:
            subscription += 1

    if subscription == 1:
        await call.message.delete()
        await call.message.answer(
            f"Assalomu alaykum <b>{call.from_user.full_name}</b>\n"
            f"Siz botdan foydalanishingiz mumkin\n"
            f"<b>Quyidagi bo'limlardan birini tanlang 👇👇👇</b>", reply_markup=menuKeyboard
        )
    else:
        await call.answer(text="Botdan foydalanish uchun barcha kanallarga obuna bo'ling!!!", show_alert=True)

        


# @dp.message_handler(state=AddState.add_user1)
# async def add_us(msg: types.Message, state: FSMContext):
#     try:
#         message = msg.text.split()
#         id = message[0]
#         name = message[1]
#         try:
#             db.add_user(id=id, name=name)
#             await state.finish()
#             await msg.answer("Foydalanuvchi bazaga qo'shildi")
#         except sqlite3.IntegrityError as err:
#             await bot.send_message(chat_id=982935447, text=err)
#             await state.finish()
#     except:
#         await msg.reply("Nimadur xato ketti")
#         await state.finish()
