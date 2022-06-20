import logging

from aiogram import Bot, Dispatcher, executor, types
from asgiref.sync import sync_to_async

from .keyboards.keyboard import kb_client
from ..user.models import TelegramUser

API_TOKEN = '5497853885:AAH7HFM2zgSsXMn_qVM-DBCyz_OLVXcTphs'

# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


# ****************КЛИЕНТСКАЯ ЧАСТЬ************

@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    user = message.from_user

    bd_user = await sync_to_async(
        TelegramUser.objects.get,
        thread_sensitive=True
    )(
        chat_id=message.from_user.id
    )
    if not bd_user:
        await sync_to_async(
            TelegramUser.objects.create,
            thread_sensitive=True
        )(
            chat_id=user.id,
            first_name=user.first_name,
            last_name=user.last_name
        )
        await message.reply(
            f"Hello my Friend, {user.full_name}",
            reply_markup=kb_client
        )
    else:
        await message.reply(
            f"You are welcome, {bd_user.first_name} {bd_user.last_name}",
            reply_markup=kb_client
        )


@dp.message_handler(lambda message: message.text and 'мои данные' in message.text.lower())
async def my_data(message: types.Message):
    user = await sync_to_async(
        TelegramUser.objects.get,
        thread_sensitive=True
    )(
        chat_id=message.from_user.id
    )
    await bot.send_message(message.from_user.id, f'First name:{user.first_name}, Last name:{user.last_name}')


@dp.message_handler(commands=['Monday'])
async def the_day_of_training(message: types.Message):
    await bot.send_message(message.from_user.id, 'This day is worker dewrewrweray in this day eou clear romm')


@dp.message_handler(commands=['Thuesday'])
async def the_next_day_of_training(message: types.Message):
    await bot.send_message(message.from_user.id, 'This day is workвпer пвапвыпday in this day eou clear romm')


@dp.message_handler(commands=['Wednesday'])
async def the_next_day_of_training1(message: types.Message):
    await bot.send_message(message.from_user.id, 'This day is worker dayкеупыва in this day eou clear romm')


@dp.message_handler(commands=['Thursday'])
async def the_next_day_of_training2(message: types.Message):
    await bot.send_message(message.from_user.id, 'This day is wеуекукпorker day in this day eou clear romm')


@dp.message_handler(commands=['Friday'])
async def the_next_day_of_training3(message: types.Message):
    await bot.send_message(message.from_user.id, 'This day is worker day in авпавыпthis day eou clear romm')


@dp.message_handler(commands=['Saturday'])
async def the_next_day_of_training4(message: types.Message):
    await bot.send_message(message.from_user.id, 'This day is worker daпавыпыавy in this day eou clear romm')


@dp.message_handler(commands=['Sunday'])
async def the_next_day_of_training5(message: types.Message):
    await bot.send_message(message.from_user.id, 'This day is worker daавпваыпy in this day eou clear romm')


@dp.message_handler()
async def echo_send(message: types.Message):
    if message.text == 'privet':
        await message.answer('Pa')


def register_handlers_client(dp: Dispatcher):
    dp.register_message_handler(send_welcome, commands=['start', 'help'])
    dp.register_message_handler(the_day_of_training, commands=['Monday'])
    dp.register_message_handler(the_next_day_of_training, commands=['Thuesday'])
    dp.register_message_handler(the_next_day_of_training1, commands=['Wednesday'])
    dp.register_message_handler(the_next_day_of_training2, commands=['Thursday'])
    dp.register_message_handler(the_next_day_of_training3, commands=['Friday'])
    dp.register_message_handler(the_next_day_of_training4, commands=['Saturday'])
    dp.register_message_handler(the_next_day_of_training5, commands=['Sunday'])
