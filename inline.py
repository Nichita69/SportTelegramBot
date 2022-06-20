# from aiogram import Bot,types
# from aiogram.dispatcher import Dispatcher
# from aiogram.utils import executor
# import os
#
# from aiogram.types import InlineKeyboardMarkup,InlineKeyboardButton
#
# bot=Bot(token=os.getenv('TOKEN'))
# dp = Dispatcher(bot)
#
# urlkb = InlineKeyboardMarkup(row_width=2)
# urlButton = InlineKeyboardButton(text='Silka',url='https://youtu.be/gpCIfQUbYlY')
# urlButton2 = InlineKeyboardButton(text='Silka',url='https://youtu.be/mhwmB95EX1A')
# urlkb.add(urlButton,urlButton2)
#
# @dp.message_handler(commands='ссылки')
# async def url_command(message : types.Message)