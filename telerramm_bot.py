import telebot
import random as r

from asciiDrawer import create

bot = telebot.TeleBot('6808053898:AAHOw7AqsmhRwjuGbz1cueWYRn0oIIT0n9M')



def HAHA():
    st=["HA","Ha","ha","ha"]
    rand=r.randint(1,15)
    ans=""
    for i in range(rand):
        ans+=st[r.randint(0,3)]
    return (ans)


@bot.message_handler(commands= ["haha"] )
def main(message):
    bot.send_message(message.chat.id, HAHA())

@bot.message_handler(commands=['start'])
def begin(message):
    bot.send_message(message.chat.id, '<em>Hello, my Darling</em>! \n Print "/help" if you wanna check all my commands!', parse_mode='html')

@bot.message_handler(commands=['sites'])
def vivod_comand(message):
    bot.send_message(message.chat.id,'What site do you want?\n /kalkul_matric\n /sinonimaizer\n /anti_copy_plagiat\n /free_IT_courses\n /best_kalkul\n /sleep_manager\n /spargalka\n')

@bot.message_handler(commands=['kalkul_matric', 'sinonimaizer', 'anti_copy_plagiat', 'free_IT_courses', 'best_kalkul', 'sleep_manager', 'spargalka'])
def sites(message):
    if message.text == '/kalkul_matric':
        bot.send_message(message.chat.id, '<a href="https://ru.onlinemschool.com/math/assistance/matrix/multiply/">kalkul_matric</a>', parse_mode='html')
    elif message.text == '/sinonimaizer':
        bot.send_message(message.chat.id,'<a href="https://maxtext.ru/sinonimaizer-teksta-online">sinonimaizer</a>', parse_mode='html')
    elif message.text == '/free_IT_courses':
        bot.send_message(message.chat.id, '<a href="https://stepik.org/catalog">free_IT_courses</a>', parse_mode='html')
    elif message.text == '/best_kalkul':
        bot.send_message(message.chat.id, '<a href="https://www.mathway.com/ru/Algebra">best_kalkul</a>', parse_mode='html')
    elif message.text == '/anti_copy_plagiat':
        bot.send_message(message.chat.id, '<a href="https://text.ru/antiplagiat">anti_copy_plagiat</a>', parse_mode='html')
    elif message.text == '/sleep_manager':
        bot.send_message(message.chat.id, '<a href="https://sleepytime.cc/">sleep_manager</a>', parse_mode='html')
    elif message.text == '/spargalka':
        bot.send_message(message.chat.id, '<a href="https://cheatography.com/">spargalka</a>', parse_mode='html')

@bot.message_handler(commands=['infa'])
def main(message):
    bot.send_message(message.chat.id, 'Это бот создан Sam1q, Allorin, cubikRUbik и Black_lenin. Надеемся, что функционал вам понравится!❤️')

@bot.message_handler(commands=['help'])
def start(message):
    bot.send_message(message.chat.id, 'Список моих команд:\n /start\n /sites\n /infa\n /haha\n')

@bot.message_handler(content_types=['photo'])
def start(message):
    file_path = bot.get_file(message.photo[-1].file_id).file_path
    file = bot.download_file(file_path)
    with open("userPhoto.png", "wb") as code:
        code.write(file)
    create('userPhoto.png')
    bot.send_photo(message.chat.id, open('./output.png', 'rb'))


bot.polling(none_stop = True)