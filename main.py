import asyncio
from idlelib.undo import Command

from aiogram import F, Bot, Dispatcher, types

from settings import TELEGRAM_TOKEN

bot = Bot(TELEGRAM_TOKEN)

dp = Dispatcher()


@dp.message(Command("start"))
async def start(message: types.Message):
    """ Функция для запуска проекта """
    kb = [
        [
            types.InlineKeyboardButton(text="Каталгог", callback_data='catalog')
        ],
        [
            types.InlineKeyboardButton(text="Профиль", callback_data='profile'),
            types.InlineKeyboardButton(text="О нас", callback_data='about'),
        ],
        [
            types.InlineKeyboardButton(text="Тех.поддержка", callback_data='support')
        ]
    ]
    keyboard = types.InlineKeyboardMarkup(inline_keyboard=kb)
    await message.answer('Привет! Это онлайн магазина', reply_markup=keyboard)


@dp.callback_query(F.data == 'catalog')
async def catalog_callback(callback: types.CallbackQuery):
    """ Функция отображения каталога курсов """
    kb2 = [
        [
            types.InlineKeyboardButton(text="Python", callback_data='python'),
            types.InlineKeyboardButton(text="Aiogram", callback_data='aiogram'),
        ],
        [
            types.InlineKeyboardButton(text="Django", callback_data='django'),
            types.InlineKeyboardButton(text="Telebot", callback_data='telebot')
        ]
    ]
    keyboard_curs = types.InlineKeyboardMarkup(inline_keyboard=kb2)
    await callback.message.answer('Выберите курс для покупки', reply_markup=keyboard_curs)


@dp.callback_query(F.data == 'about')
async def about_me_callback(callback: types.CallbackQuery):
    """ Функция отображения информации о магазине """
    await callback.message.answer(
        'Магазин онлайн курсов по программированию, сдесь ты может приобрести курс или перейти на наш сайт.')


async def main():
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
