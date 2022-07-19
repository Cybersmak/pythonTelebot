import logging 
from aiogram import Bot, Dispatcher, executor, types
import markups as nav
from DataBase import Database
import os
import subprocess
import glob

TOKEN = '5527562178:AAFHrWRmBQk1ZzhuBzv1hhKvONjvnl4U8ns'

logging.basicConfig(level = logging.INFO)

bot = Bot(TOKEN)
dp = Dispatcher(bot)

db = Database('DataBase.db')

@dp.message_handler(commands = ['start'])

async def start(message: types.Message):
    if(not db.user_exists(message.from_user.id)):
        db.add_user(message.from_user.id)
        await bot.send_message(message.from_user.id, "Укажите ваше Имя")

    else:
        await bot.send_message(message.from_user.id, "Вы уже зарегистрированы!",reply_markup = nav.mainMenu)  

             



@dp.message_handler()

async def bot_message(message: types.Message):
    if message.chat.type == 'private':
        if message.text == 'ПРОФИЛЬ':
            user_name = "Ваше имя: "+ db.get_name(message.from_user.id)
            user_phone = "Ваш номер телефона: "+db.get_phone(message.from_user.id)
            user_key = "ваш ключ: "+db.get_key(message.from_user.id)
            await bot.send_message(message.from_user.id,user_name)
            await bot.send_message(message.from_user.id,user_phone)
            await bot.send_message(message.from_user.id,user_key)


        else:
            if db.get_signup(message.from_user.id) == "setName":
                if(len(message.text)>59):
                    await bot.send_message(message.from_user.id, "Имя не должно превышать 25 символов")
                elif '@' in message.text or '/' in message.text:
                    await bot.send_message(message.from_user.id, "Вы ввели запрешенный символ")
                else:
                    db.set_name(message.from_user.id,message.text)
                    db.set_signup(message.from_user.id,'done')
                    await bot.send_message(message.from_user.id,"Укажите ваш номр телефона")   

        
            elif db.get_phone(message.from_user.id) == "setPhone":
                if(len(message.text)>29):
                    await bot.send_message(message.from_user.id, "Номер телефона не должно превышать 29 символов")
                elif '@' in message.text or '/' in message.text:
                    await bot.send_message(message.from_user.id, "Вы ввели запрешенный символ")
                else:
                    db.set_phone(message.from_user.id,message.text)
                    await bot.send_message(message.from_user.id,"Укажите ваш ключ к файлам")


            elif db.get_key(message.from_user.id) == "setKey":   
                if(len(message.text)>50):
                    await bot.send_message(message.from_user.id, "Ключ доступа не должно превышать 50 символов")
                elif '@' in message.text or '/' in message.text:
                    await bot.send_message(message.from_user.id, "Вы ввели запрешенный символ")
                else:
                    db.set_key(message.from_user.id,message.text)
                    await bot.send_message(message.from_user.id,"Поздравляю вы успешно зарегистрированы!", reply_markup = nav.mainMenu) 

        
        # if message.text == 'Сводные показатели':
        #     path = r'\\dalimo.ru\1c\PDAFILES\OUT_FTP\Reports'
        #     os.chdir(path)
        #     files=glob.glob('*.html')
        #     for filename in files:
        #         id = filename[:-11]  
        #         sd = id + '_dolgi.html'
        #         if db.get_key1(message.from_user.id) == id:
        #             document = open(sd, 'rb')
        #             await bot.send_document(message.from_user.id,document, reply_markup = nav.mainMenu)


                            
            else:
                # await bot.send_message(message.from_user.id, "Повторите попытку")
                path = r'\\dalimo.ru\1c\PDAFILES\OUT_FTP\Reports'
                os.chdir(path)
                sd = db.get_key1(message.from_user.id)
                for row in sd:
                    files = row + "_dolgi.html"
                    document = open(files, 'rb')
                await bot.send_document(message.from_user.id,document, reply_markup = nav.mainMenu)




# @dp.message_handler(commands = [''])

# async def get_files(message:types.Message):
#         if message.text == 'Сводные показатели':
#             path = r'\\dalimo.ru\1c\PDAFILES\OUT_FTP\Reports'
#             os.chdir(path)
#             # files=glob.glob('*.html')
#             # for filename in files:
#             #     id = filename[:-11]  
#             #     sd = id + '_dolgi.html'
#             #     if db.get_key == id:
#             document = open(f'K00165_dolgi.html', 'rb')
#             await bot.send_document(message.from_user.id,document, reply_markup = nav.mainMenu)

if __name__=="__main__":
    executor.start_polling(dp,skip_updates = True)