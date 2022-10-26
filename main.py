import random
from config import stands
from config import link
from config import two
from config import three
from config import four
from config import five
from config import six
from config import seven
from config import eight
from config import ike
from config import eoch
from config import durt
from config import bish
from config import alti
from config import ghide
from config import sigez
from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
from aiogram.types import Message, CallbackQuery, InputMedia
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
#WTF

TOKEN = ('5399899287:AAE-apYTLr9JooW23NdAgdqV1NA-zBvCo4c')
bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

inkb = InlineKeyboardMarkup(row_width=1).add(InlineKeyboardButton(text='Нажми на меня', callback_data='www'))


@dp.message_handler(commands=["start"])
async def photo(message: Message):
    user_id = message.from_user.id
    if user_id == 1452627274:
        await bot.send_message(message.from_user.id, 'О! Динар, добро пожаловать')
        reply_markup = InlineKeyboardMarkup().add(
            InlineKeyboardButton(text="Стенд стрела", callback_data="Stand_arr"),
            InlineKeyboardButton(text="Таинственная стрела", callback_data="Mystery_arr"),
            InlineKeyboardButton(text="Чтобы узнать в чем их разница, нажмите сюда", callback_data="info")
        )
        photo_url = 'https://static.jojowiki.com/images/6/62/latest/20200308004007/Arrowheads_anime.png'

        await bot.send_photo(
            message.chat.id,
            photo=photo_url,
            reply_markup=reply_markup,
            caption="Вы нашли две стрелы, какую хотите использовать?",
        )
    else:
        await bot.send_message(message.from_user.id, 'Ты не Динар, проваливай')

@dp.callback_query_handler(text="Stand_arr")
async def photo_update(query: CallbackQuery):
    new_url = 'https://www.mirf.ru/wp-content/uploads/2021/04/JoJos-Bizarre-Adventure-3.jpg'
    reply_markup = InlineKeyboardMarkup().add(
        InlineKeyboardButton(text="1", callback_data="season1"),
        InlineKeyboardButton(text="2", callback_data="season2"),
        InlineKeyboardButton(text="3", callback_data="season3"),
        InlineKeyboardButton(text="4", callback_data="season4"),
        InlineKeyboardButton(text="5", callback_data="season5"),
        InlineKeyboardButton(text="6", callback_data="season6"),
        InlineKeyboardButton(text="7", callback_data="season7"),
        InlineKeyboardButton(text="8", callback_data="season8")
    )
    url = InputMedia(media=new_url, caption="Какой сезон ты выберишь?")

    await query.message.edit_media(url, reply_markup=reply_markup)

@dp.callback_query_handler(text=['season1'])
async def season1_command(message: types.Message):
    await bot.send_message(message.from_user.id, 'В первом сезоне стендов нет')
@dp.callback_query_handler(text=['season2'])
async def season2_command(message: types.Message):
    chat_id = message.from_user.id
    photo_url = ike['0']
    await dp.bot.send_photo(chat_id=chat_id, photo=photo_url, caption=f"Твой стенд это {two['0']}")
@dp.callback_query_handler(text=['season3'])
async def season3_command(message: types.Message):
    chat_id = message.from_user.id
    photo_url = eoch['0']
    await dp.bot.send_photo(chat_id=chat_id, photo=photo_url, caption=f"Твой стенд это {three['0']}")
@dp.callback_query_handler(text=['season4'])
async def season4_command(message: types.Message):
    chat_id = message.from_user.id
    photo_url = durt['0']
    await dp.bot.send_photo(chat_id=chat_id, photo=photo_url, caption=f"Твой стенд это {four['0']}")
@dp.callback_query_handler(text=['season5'])
async def season5_command(message: types.Message):
    chat_id = message.from_user.id
    photo_url = bish['0']
    await dp.bot.send_photo(chat_id=chat_id, photo=photo_url, caption=f"Твой стенд это {five['0']}")
@dp.callback_query_handler(text=['season6'])
async def season6_command(message: types.Message):
    chat_id = message.from_user.id
    photo_url = alti['0']
    await dp.bot.send_photo(chat_id=chat_id, photo=photo_url, caption=f"Твой стенд это {six['0']}")
@dp.callback_query_handler(text=['season7'])
async def season7_command(message: types.Message):
    chat_id = message.from_user.id
    photo_url = ghide['0']
    await dp.bot.send_photo(chat_id=chat_id, photo=photo_url, caption=f"Твой стенд это {seven['0']}")
@dp.callback_query_handler(text=['season8'])
async def season8_command(message: types.Message):
    chat_id = message.from_user.id
    photo_url = sigez['0']
    await dp.bot.send_photo(chat_id=chat_id, photo=photo_url, caption=f"Твой стенд это {eight['0']}")

@dp.callback_query_handler(text='Mystery_arr')
async def send_photo(message: Message):
    chat_id = message.from_user.id
    st_num = str(random.randint(0, 2))
    photo_url = link[st_num]
    stand = stands[st_num]
    await dp.bot.send_photo(chat_id=chat_id, photo=photo_url, caption=f"Твой стенд это {stand}")

@dp.callback_query_handler(text=['info'])
async def season1_command(message: types.Message):
    await bot.send_message(message.from_user.id,
                           "Стенд стрела - позволяет получить стенд из определённого сезона по твоему желанию\nТаинственная стрела - позволяет получить рандомный стенд из всех сезонов аниме")

if __name__ == '__main__':
   executor.start_polling(dp)