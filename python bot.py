import logging
import os
from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup

API_TOKEN = os.getenv('API_TOKEN')
CHAT_ID = int(os.getenv('CHAT_ID'))

logging.basicConfig(level=logging.INFO)

bot = Bot(token=API_TOKEN)
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)

class Form(StatesGroup):
    name = State()
    phone = State()

@dp.message_handler(commands='start')
async def cmd_start(message: types.Message):
    await Form.name.set()
    await message.reply("Введите ваше имя:")

@dp.message_handler(state=Form.name)
async def process_name(message: types.Message, state: FSMContext):
    await state.update_data(name=message.text)
    await Form.phone.set()
    await message.reply("Введите ваш телефон:")

@dp.message_handler(state=Form.phone)
async def process_phone(message: types.Message, state: FSMContext):
    await state.update_data(phone=message.text)
    data = await state.get_data()
    name = data['name']
    phone = data['phone']

    text = f"📥 Новая заявка:\n\n👤 Имя: {name}\n📞 Телефон: {phone}"
    await bot.send_message(CHAT_ID, text)

    await message.reply("✅ Спасибо! Смета отправлена на скачивание.")
    await state.finish()

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
