from aiogram import Router,F
from aiogram.fsm.context import FSMContext
from app.keyboard import menu
from app.fsm_group import Sign_Up
import os
from dotenv import load_dotenv

load_dotenv()
CHAT_ID = os.getenv('CHANNEL_ID')

router = Router()

@router.message(F.text == '/start')
async def start_command(msg):
    await msg.answer('Привет.Хотите записаться на стрижку?',reply_markup=menu)

@router.message(F.text == 'О нас')
async def about_us(msg):
    await msg.answer('Мы парикмахерская "Стрижка".Мы работаем с 9:00 до 21:00 без выходных.Имеем многолетний опыт работы в сфере парикмахерских услуг.')

@router.message(F.text == 'Контакты')
async def contacts(msg):
    await msg.answer('Наш адрес:Улица Пушкина,дом Колотушкина.\nТелефон для записи:88055545')
                     
@router.message(F.text == 'Записаться на стрижку')
async def sign_up(msg,state:FSMContext):
    await msg.answer('Хорошо,тогда я сейчас проведу регистрацию.')
    await msg.answer('Как вас зовут?')
    await state.set_state(Sign_Up.number)

@router.message(Sign_Up.number)
async def sign_up_number(msg,state:FSMContext):
    await state.update_data(name=msg.text)
    await msg.answer('Введите номер телефона:')
    await state.set_state(Sign_Up.haircut)

@router.message(Sign_Up.haircut)
async def sign_up_haitcut(msg,state:FSMContext):
    await state.update_data(phone=msg.text)
    await msg.answer('Вы хотите сразу назвать как вас подстричь или всю информацию скажите в самом заведении?(Ввести Да/Нет).На какое время хотите записаться?')
    await state.set_state(Sign_Up.yes_no)

@router.message(Sign_Up.yes_no)
async def sign_up_yes_no(msg,state:FSMContext):
    if msg.text.lower() in ['да']:
        await msg.answer('Тогда опишите как вы хотите подстриться:')
        await state.set_state(Sign_Up.result_yes)
    elif msg.text.lower() in ['нет']:
        await msg.answer('Спасибо за сотрудничество и ждём у нас!')

@router.message(Sign_Up.result_yes)
async def sign_up_result_yes(msg,state:FSMContext):
    user_data = await state.get_data()
    name = user_data.get('name', 'Не указано')
    phone = user_data.get('phone', 'Не указано')
    wishes = msg.text
    chat_id = int(CHAT_ID)
    await msg.bot.send_message(chat_id,f'Сообщение от пользователя:{name}\nНомер телефона:{phone}\nПожелания:{wishes}')
    await msg.answer('Ваше сообщение было отправлено.Спасибо за сотрудничество')
