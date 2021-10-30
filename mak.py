import random
import telebot
from telebot import types

bot = telebot.TeleBot("1879287626:AAFgmAAdP2PSfnhLdByELQtuAAl0_bWAGoo")
def c(word):
    t = ""
    r = random.randint(0,2)
    lst = ["!!","..",",,"][r]
    for one in word:
        t += f" {lst} {one}"
    return t

def do(word):
    if word.count("1") or word.count("2") or word.count("3") or word.count("4") or word.count("5") or word.count("6") or word.count("7") or word.count("8") or word.count("9") or word.count("0"):
        return True
    else:
        return False

sudo = "bzzzw","WLLLDE"

def add(message):
    open("makalat.txt","a+",encoding="utf-8").write(f"\n{message.text}")
    bot.reply_to(message,f"- تم اضافة المقال : \n{message.text}")
def delete(message):
    bot.reply_to(message,"- تم ارسال الطلب للحذف .")
    open("want.txt","a+").write(f"\n{message.text}")
@bot.message_handler(commands=['start'])
def start(message):
    keyboard = types.InlineKeyboardMarkup(row_width=2)
    callback_button = types.InlineKeyboardButton(text="اضف البوت لقروبك .", url="http://t.me/?startgroup=new")
    callback_button2 = types.InlineKeyboardButton(text="المطور .", url="https://t.me/bzzzw")
    callback_button3 = types.InlineKeyboardButton(text="قناة المطور .", url="https://t.me/biiir")
    keyboard.add(callback_button, callback_button2, callback_button3)
    user = message.from_user.first_name
    bot.send_message(message.chat.id,f"- هلا والله {user} ."
                                     f"\n\n"
                                     f"- ضيفني لقروبك واستمتع .."
                                     f"\n"
                                     f"\n"
                                     f"- مقالات عاديه انقليزي من 1 الى 1000 ."
                                     f"\n"
                                     f"- مقالات عكسيه عربي من 1 الى 1000\n\n"
                                     f"- تبي تدرب بلخاص حق البوت ؟ اكتب /go",reply_to_message_id=message.message_id,reply_markup=keyboard)
@bot.message_handler(func=lambda m: True)
def mak(message):
    sot = do(message.text)
    if sot == True:
        try:
            r = open(f"{message.chat.id}.txt","r").read()
            if r == "True":
                so = open("makalat.txt", "r", encoding="utf-8").read().splitlines()[int(message.text)].split()
                m = bot.send_message(message.chat.id, c(so), reply_to_message_id=message.message_id)
        except:
            pass
    if message.text "/go":
    	bot.reply_to(message,"قريبا")
    if message.chat.type == "group" or message.chat.type == "supergroup":
        if message.text ==  "تعطيل بوت المقالات" and bot.get_chat_member(message.chat.id,message.from_user.id).status in ['administrator','creator']:
            open(f"{message.chat.id}.txt","w+").write(f"False")
            bot.reply_to(message,f"- من قبل {message.from_user.first_name} تم تعطيل البوت بلمجموعة .")
        if message.text == "تفعيل بوت المقالات" and bot.get_chat_member(message.chat.id,message.from_user.id).status in ['administrator','creator']:
            open(f"{message.chat.id}.txt","w+").write(f"True")
            bot.reply_to(message, f"- من قبل {message.from_user.first_name} تم تفعيل البوت بلمجموعة .")
        if message.text == "مقالات":
            s2o = open("makalat.txt", "r", encoding="utf-8").read()
            r = random.randint(0, 2)
            so = open("makalat.txt","r",encoding="utf-8").read().splitlines()[int(r)].split()
            bot.send_message(message.chat.id,c(so),reply_to_message_id=message.message_id)
        if message.text == "اضف مقال" and message.from_user.username in sudo:
            dine = bot.reply_to(message,"- دن ارسل المقال .")
            bot.register_next_step_handler(dine,add)
        if message.text ==   "المقالات" and message.from_user.username in sudo:
            all = open("makalat.txt","r").readlines()
            bot.send_message(message.chat.id,reply_to_message_id=message.message_id,text=f"- عدد المقالات كامله : {len(all)}")
        if message.text == "حذف مقال" and message.from_user.username == sudo:
            me = bot.reply_to(message,f"- ارسل المقال لحذفه ي عزيزي .")
            bot.register_next_step_handler(me,delete)

def got(message):
    bot.reply_to(message,f"- اسرع ياوحش يلا خذ ذي المقاله .")
    s2o = open("makalat.txt", "r", encoding="utf-8").read()
    r = random.randint(0,2)
    so = open("makalat.txt", "r", encoding="utf-8").read().splitlines()[int(r)].split()
    m = bot.send_message(message.chat.id, c(so), reply_to_message_id=message.message_id)
    bot.register_next_step_handler(m, got)
bot.polling(True)
