import config
import telebot #pip3 install pyTelegramBotAPI
import os
import time

bot = telebot.TeleBot(config.token) #write your bot token into the brackets !!!ATENTION!!! Never share your bot token!!!
filesize = os.path.getsize('shopping.txt')
ignore_yn = True

ynkey = telebot.types.ReplyKeyboardMarkup(True)
ynkey.row('Yes', 'No')

basekey = telebot.types.ReplyKeyboardMarkup(True)
basekey.row('/show', '/start', '/clear')

def list_clear():
    myfile = open('shopping.txt', 'w')
    myfile.write('''''')
    myfile.close()

def list_add(thing):
    myfile = open('shopping.txt', 'a')
    myfile.write(thing)
    myfile.write('''
''')
    myfile.close()

def list_show():
    myfile = open('shopping.txt', 'r')
    all_list = ''''''
    num = 1
    for line in myfile.readlines():
        all_list = all_list + str(num)
        all_list = all_list + ')'
        all_list = all_list + ' '
        num += 1
        all_list = all_list + line[:-1]
        all_list = all_list + '''
'''
        myfile.close()
    return all_list

def list_rem(line):
    myfile = open('shopping.txt', 'r')
    lines = myfile.readlines()
    myfile.close()
    
    del lines[line]
    
    newf = open('shopping.txt', 'w+')
    for line in lines:
        newf.write(line)
    newf.close()

@bot.message_handler(commands=['start'])
def start_command(message):
    try:
        bot.send_message(message.chat.id, 'Welcome via de familia!', reply_markup=basekey)
    except OSError:
        bot.send_message(message.chat.id, 'Welcome via de familia!', reply_markup=basekey)

@bot.message_handler(commands=['add'])
def add_command(message):
    list_add(message.text[5:])

@bot.message_handler(commands=['remove'])
def rem_command(message):
    list_rem(int(message.text[7:])-1)
    try:
        bot.send_message(message.chat.id, 'Deleted')
    except OSError:
        bot.send_message(message.chat.id, 'Deleted')

@bot.message_handler(commands=['clear'])
def clear_command(message):
    global ignore_yn
    ignore_yn = False
    try:
        bot.send_message(message.chat.id, 'Are you shure you want to erase all your shopping list?', reply_markup=ynkey)
    except OSError:
        bot.send_message(message.chat.id, 'Are you shure you want to erase all your shopping list?', reply_markup=ynkey)

@bot.message_handler(commands=['show'])
def show_command(message):
    result = list_show()
    filesize = os.path.getsize('shopping.txt')
    if filesize == 0:
        try:
            bot.send_message(message.chat.id, 'Your shopping list is empty!')
        except OSError:
            bot.send_message(message.chat.id, 'Your shopping list is empty!')
    else:
        try:
            bot.send_message(message.chat.id, result)
        except OSError:
            bot.send_message(message.chat.id, result)

@bot.message_handler(content_types=["text"])        
def anwser_message(message):
    global ignore_yn
    if ignore_yn == False:
        if message.text == 'Yes':
            try:
                bot.send_message(message.chat.id, 'Ok, I erased all your shopping list!', reply_markup=basekey)
                list_clear()
            except OSError:
                bot.send_message(message.chat.id, 'Ok, I erased all your shopping list!', reply_markup=basekey)
                list_clear()

        elif message.text == 'No':
            try:
                bot.send_message(message.chat.id, 'Ok, I left your shopping list how it was!', reply_markup=basekey)
            except OSError:
                bot.send_message(message.chat.id, 'Ok, I left your shopping list how it was!', reply_markup=basekeyy)
        
        ignore_yn = True

bot.polling()
