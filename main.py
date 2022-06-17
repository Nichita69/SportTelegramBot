import logging

from aiogram import Bot, Dispatcher, executor, types
from keyboards import kb_client

API_TOKEN = '5497853885:AAH7HFM2zgSsXMn_qVM-DBCyz_OLVXcTphs'

# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


async def on_startup(_):
    print('Бот вышел в онлайн')


# ****************КЛИЕНТСКАЯ ЧАСТЬ************

@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    await message.reply(f"Hello my Friend, {message.from_user.first_name} {message.from_user.last_name}",
                        reply_markup=kb_client)


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


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True, on_startup=on_startup)
