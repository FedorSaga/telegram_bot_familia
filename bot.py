import config
import telebot

def list_add(thing):
    myfile = open('shopping.txt', 'a')
    myfile.write(thing)
    myfile.write('''
''')
    myfile.close()

def list_show():
    myfile = open('shopping.txt', 'r')
    all_list = ''''''
    for line in myfile.readlines():
        all_list = all_list + line[:-1]
        all_list = all_list + '''
'''
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

bot = telebot.TeleBot(config.token)

shopping = []

@bot.message_handler(commands=['start'])
def start_command(message):
        try:
            bot.send_message(message.chat.id, 'Welcome via de familia!')
        except OSError:
            bot.send_message(message.chat.id, 'Welcome via de familia!')

@bot.message_handler(commands=['add'])
def add_command(message):
            list_add(message.text[5:])

@bot.message_handler(commands=['remove'])
def rem_command(message):
        list_rem(int(message.text[7:])-1)

@bot.message_handler(commands=['show'])
def show_command(message):
            result = list_show()
            bot.send_message(message.chat.id, result)

bot.polling()