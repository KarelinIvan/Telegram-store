import asyncio
from aiogram import F, Bot, Dispatcher, types

from aiogram.filters import Command

from settings import TELEGRAM_TOKEN

bot = Bot(TELEGRAM_TOKEN)

dp = Dispatcher()


@dp.message(Command("start"))
async def start(message: types.Message):
    """ Функция для запуска проекта """
    kbm = [
        [
            types.InlineKeyboardButton(text="Меню магазина", callback_data='menu')
        ]
    ]
    keyboard_menu = types.InlineKeyboardMarkup(inline_keyboard=kbm)
    await message.answer(f'Привет, {message.from_user.first_name}! Это онлайн магазин курсов по праграмированию', reply_markup=keyboard_menu)


@dp.callback_query(F.data == "menu")
async def menu_callback(callback: types.CallbackQuery):
    """ Функция отображения меню магазина """
    kb = [
        [
            types.InlineKeyboardButton(text="Каталог", callback_data='catalog')
        ],
        [
            types.InlineKeyboardButton(text="Профиль", callback_data='profile'),
            types.InlineKeyboardButton(text="О нас", callback_data='about'),
        ],
        [
            types.InlineKeyboardButton(text="Тех.поддержка", callback_data='support')
        ]
    ]
    keyboard_catalog = types.InlineKeyboardMarkup(inline_keyboard=kb)
    await callback.message.answer('Меню магазина', reply_markup=keyboard_catalog)


@dp.callback_query(F.data == "catalog")
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
        ],
        [
            types.InlineKeyboardButton(text="Вернуться в меню", callback_data="menu")
        ]
    ]
    keyboard_curs = types.InlineKeyboardMarkup(inline_keyboard=kb2)
    await callback.message.answer('Выберите курс для покупки', reply_markup=keyboard_curs)


@dp.callback_query(F.data == "about")
async def about_callback(callback: types.CallbackQuery):
    """ Функция отображения информации о магазине """
    await callback.message.answer(
        'Магазин онлайн курсов по программированию, сдесь ты может приобрести курс или перейти на наш сайт.')
    

@dp.callback_query(F.data == "support")
async def support_callback(callback: types.CallbackQuery):
    """ Функция отображения информации о тех.поддержке """
    kb3 = [
        [
            types.InlineKeyboardButton(text="Написать в VK", url="https://vk.com/id578574082")
        ]
    ]
    keyboard_support = types.InlineKeyboardMarkup(inline_keyboard=kb3)
    text = "Если у вас возникли вопросы по работе с магазином, обращайтесь в нашу техническую поддержку."
    await callback.message.answer(text, reply_markup=keyboard_support)


async def main():
    await dp.start_polling(bot)



if __name__ == "__main__":
    asyncio.run(main())
