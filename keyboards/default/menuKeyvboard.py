from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


menuKeyboard = ReplyKeyboardMarkup(
    resize_keyboard=True,
    keyboard=[
        [
            KeyboardButton(text="🎇 Effect"),
        ],
        [
            KeyboardButton(text="👨‍💻 Admin bilan bog'lanish")
        ]
    ]
)