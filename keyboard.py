from aiogram.types import ReplyKeyboardMarkup,KeyboardButton

menu = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text='О нас')],
        [KeyboardButton(text='Контакты')],
        [KeyboardButton(text='Записаться на стрижку')],
    ],
    resize_keyboard=True,
    one_time_keyboard=True
)
