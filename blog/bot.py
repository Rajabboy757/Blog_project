import logging
#from aiogram.methods import SendMessage

from aiogram import Bot, Dispatcher, executor, types
from aiogram.dispatcher.webhook import SendMessage

API_TOKEN = '5493245817:AAHhURZXfNo2u_Qsh5HoOrYNBiMFDjwoFmc'
#chat_id

# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    """
    This handler will be called when user sends `/start` or `/help` command
    """
    await message.reply("Hi!\nYou are in POWER LEADs bot.")

@dp.message_handler()
async def echo(message: types.Message):

    await message.answer(message.text.upper())
    #await message.answer(message.chat.id)

async def sendd(title, body, auth):
    author = str(auth)
    text = f"TITLE: {title} \n\nTEXT: {body} \n\nAUTHOR: {author}"

    await bot.send_message(268995218, text)
    await bot.send_message(-514166497, text)
if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
