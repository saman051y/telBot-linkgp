from message_and_text.text import *
from message_and_text.bot_messages import *
##############
def make_user_info (username,user_id,balance,score):
     text=f"""👤 نام کاربری : <a href='tg://user?id={user_id}'>{username}</a>
🆔 شناسه کاربری :<code>{user_id}</code>
💵 موجودی : {balance} هزار تومان
💯 امتیاز شما: {score}"""
     return text


def get_pic_receipt_msg(index):
    text=f"""لطفا عکس رسید خود را ارسال کنید
{make_line}
{cart_info_text}
💵 مبلغ انتخاب شده: {plans[index]} هزار تومان
"""
    return text

def select_plan_msg(index):
     text=select_plan_text=f"""{cart_info_text}
💵 مبلغ انتخاب شده: {plans[index]} هزار تومان
{make_line}
برای ارسال عکس رسید از دکمه زیر استفاده کنید"""
     return text
################################3
def make_change_score_text(score:int,convert_able:int,value:int):
     text=f"""کل امتیاز شما : {score} ✨
امتیاز قابل تبدیل : {convert_able} ♻️ معادل : {value} هزار تومان💵"""
     return text