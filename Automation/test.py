import logging 
from aiogram import Bot, Dispatcher, executor, types
import markups as nav
from DataBase import Database
import os
import subprocess
import glob

TOKEN = '5527562178:AAFHrWRmBQk1ZzhuBzv1hhKvONjvnl4U8ns'
bot = Bot(TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands = ['start'])

async def get_files(message:types.Message):
    # if message.chat.type == 'private':
    #     if message.text == 'Сводные показатели':
    path = r'\\dalimo.ru\1c\PDAFILES\OUT_FTP\Reports'
    os.chdir(path)
    #         files=glob.glob('*.html')
    #         for filename in files:
    #             id = filename[:-11]  
    #             sd = id + '_dolgi.html'
    #             if db.get_key == id:
    #                 document = open(sd,"rb",)
    document = open(f'K00165_dolgi.html', 'rb')
    await bot.send_document(message.from_user.id,document)

if __name__=="__main__":
    executor.start_polling(dp,skip_updates = True)