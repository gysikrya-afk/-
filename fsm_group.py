from aiogram.fsm.state import State,StatesGroup

class Sign_Up(StatesGroup):
    name = State()
    number = State()
    haircut = State()
    yes_no = State()
    result_yes = State()
