import logging

from aiogram import Bot, Dispatcher, executor, types
from buttons import *

API_TOKEN = '6201314113:AAEtATkTCXxrWxLIZ7Ml4cSinTygyEApuc4'

logging.basicConfig(level=logging.INFO)

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def echo(message: types.Message):
    await message.answer("Добро пожаловать в бот Mars!\nПожалуйста укажите кем вы являетесь))",reply_markup=bosh_menu)

@dp.callback_query_handler(text="Ota ona")
async def echo(call: types.CallbackQuery):
    await call.message.answer("Добро пожаловать в бот Mars! Пожалуйста, выберите опцию", reply_markup=ota_ona_keyboard)

@dp.callback_query_handler(text="O'quvchi")
async def echo(call: types.CallbackQuery):
    await call.message.answer("Введите свой id Modme")

@dp.callback_query_handler(text="Mehmon")
async def echo(call: types.CallbackQuery):
    await call.message.answer("Добро пожаловать в бот Mars! Пожалуйста, выберите опцию", reply_markup=oquvchi_keyboard)

@dp.message_handler(text="📍 Филиалы")
async def echo(message: types.message):
    await message.answer("""У нас есть два филиала.

📍Филиал Тинчлик
Адрес: г.Ташкент, метро Тинчлик, Беруний 35 А
Телефон:
+998954105054
+998954115054

📍Филиал Юнусабад
Юнусабадский район, Строй центр, 3 эт.
Телефон:
+998901165054
+998901175054

🗺Получить местоположения от следующих кнопок""", reply_markup=location_menu)
    
@dp.callback_query_handler(text="tinchlik")
async def echo(call: types.CallbackQuery):
    await call.message.answer_location(41.334800097924614, 69.21558046938834)
    await call.message.answer("ТИНЧЛИК")

@dp.callback_query_handler(text="yunusobod")
async def echo(call: types.CallbackQuery):
    await call.message.answer_location(41.367103538499705, 69.28601093702731)
    await call.message.answer("ЮНУСАБАД")

@dp.message_handler(text="📝 О нашых курсах")
async def echo(message: types.message):
    await message.answer_photo("https://t.me/csascdsc/2")

@dp.message_handler(text="🔥 Работы наших учеников")
async def echo(message: types.message):
    await message.answer_video("https://t.me/csascdsc/4?single")
    await message.answer_video("https://t.me/csascdsc/5")
    await message.answer_video("https://t.me/csascdsc/6?single")
    await message.answer_video("https://t.me/csascdsc/7")
    await message.answer_video("https://t.me/csascdsc/8")
    await message.answer_video("https://t.me/csascdsc/9")
    await message.answer_video("https://t.me/csascdsc/10")

@dp.message_handler(text="⭐️ Отзывы")
async def echo(message: types.message):
    await message.answer_video("https://t.me/csascdsc/11")
    await message.answer_video("https://t.me/csascdsc/12")
    await message.answer_video("https://t.me/csascdsc/13")
    await message.answer_video("https://t.me/csascdsc/14")
    await message.answer_video("https://t.me/csascdsc/15")
    await message.answer_video("https://t.me/csascdsc/11?single")

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)