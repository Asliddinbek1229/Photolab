from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

menuKeyboard = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="🎇 Effect", callback_data='effect'),
        ],
        [
            InlineKeyboardButton(text="👨‍💻 Admin bilan bog'lanish", callback_data='contact'),
        ],
    ]
)