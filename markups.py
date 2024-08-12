from configs.config import * 
from functions.custom_functions import *
from message_and_text.text import *
from telebot.types import InlineKeyboardButton ,InlineKeyboardMarkup,ReplyKeyboardMarkup,KeyboardButton,Message,CallbackQuery

########################################################################
back_button=InlineKeyboardButton(text="back",callback_data="back")
#markups
markup_join=InlineKeyboardMarkup()
button=InlineKeyboardButton(text="برسی عضویت",callback_data="proceed")
markup_join.add(button)
###!user
markup_main=ReplyKeyboardMarkup(resize_keyboard=True,row_width=2)
markup_main.add(free_rime_btn)
markup_main.add(user_acc_btn)
markup_main.add(support_btn,make_banner_btn)
###!admin
markup_main_admin=ReplyKeyboardMarkup(resize_keyboard=True,row_width=2)
markup_main_admin.add(free_rime_btn)
markup_main_admin.add(admin_btn_bot_info)
markup_main_admin.add(admin_btn_user_list,admin_btn_find_user_info)
markup_main_admin.add(admin_btn_send_msg_to_all,admin_btn_check_income)
