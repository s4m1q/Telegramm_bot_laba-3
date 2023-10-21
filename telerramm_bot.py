import telebot
bot = telebot.TeleBot('6808053898:AAHOw7AqsmhRwjuGbz1cueWYRn0oIIT0n9M')


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
    bot.send_message(message.chat.id, 'Список моих команд:\n /start\n /sites\n /infa\n')
bot.polling(none_stop = True)