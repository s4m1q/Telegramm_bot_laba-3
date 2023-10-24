import os
import telebot
import random as r

from asciiDrawer import create

bot = telebot.TeleBot('6808053898:AAHOw7AqsmhRwjuGbz1cueWYRn0oIIT0n9M')

if not os.path.exists('images'):
    os.makedirs('images')


def HAHA():
    st = ["HA", "Ha", "ha", "ha"]
    rand = r.randint(1, 15)
    ans = ""
    for i in range(rand):
        ans += st[r.randint(0, 3)]
    return (ans)


@bot.message_handler(commands=["haha"])
def main(message):
    bot.send_message(message.chat.id, HAHA())


@bot.message_handler(commands=['start'])
def begin(message):
    bot.send_message(message.chat.id,
                     '<em>Hello, my Darling</em>! \n Print "/help" if you wanna check all my commands!',
                     parse_mode='html')


@bot.message_handler(commands=['sites'])
def vivod_comand(message):
    bot.send_message(message.chat.id,
                     'What site do you want?\n /kalkul_matric\n /sinonimaizer\n /anti_copy_plagiat\n /free_IT_courses\n /best_kalkul\n /sleep_manager\n /spargalka\n')


@bot.message_handler(commands = ['kitten'])
def cat_photo(message):
    rand = r.randint(1, 23)
    for i in range(rand):
        if i == 1:
            bot.send_message(message.chat.id, "https://fanibani.ru/wp-content/uploads/2022/12/malysh-koshka.jpg")
            break
        elif i == 2:
            bot.send_message(message.chat.id, "https://fanibani.ru/wp-content/uploads/2022/12/da51384eb809ea34ea211da5d6e26a03.jpg")
            break
        elif i == 3:
            bot.send_message(message.chat.id, "https://get.pxhere.com/photo/sweet-kitten-cat-mammal-whiskers-vertebrate-babies-kittens-himalayan-persian-small-to-medium-sized-cats-cat-like-mammal-carnivoran-dog-breed-group-1074107.jpg")
            break
        elif i == 4:
            bot.send_message(message.chat.id, "https://zabavnikplus.ru/wp-content/uploads/2/6/d/26d7b18ceaf454a250283fd50d77db1c.jpeg")
            break
        elif i == 5:
            bot.send_message(message.chat.id, "https://images8.alphacoders.com/104/1049186.jpg")
            break
        elif i == 6:
            bot.send_message(message.chat.id, "https://fanibani.ru/wp-content/uploads/2022/12/sweet-kitten-cat-mammal-nose-whiskers-an-scaled.jpg")
            break
        elif i == 7:
            bot.send_message(message.chat.id, "https://ferma-biz.ru/wp-content/uploads/2022/08/scale_1200-2-1.jpg")
            break
        elif i == 8:
            bot.send_message(message.chat.id, "https://fanibani.ru/wp-content/uploads/2022/12/malenkij-pushistyj-kot-nok-myaukaet.jpg")
            break
        elif i == 9:
            bot.send_message(message.chat.id, "https://fikiwiki.com/uploads/posts/2022-02/1644827414_25-fikiwiki-com-p-kartinki-smeshnie-krasivie-i-milie-pro-kot-27.jpg")
            break
        elif i == 10:
            bot.send_message(message.chat.id, "https://fanibani.ru/wp-content/uploads/2022/12/kotionok-9-6.jpg")
            break
        elif i == 11:
            bot.send_message(message.chat.id, "https://fikiwiki.com/uploads/posts/2022-02/1644827438_37-fikiwiki-com-p-kartinki-smeshnie-krasivie-i-milie-pro-kot-39.jpg")
            break
        elif i == 12:
            bot.send_message(message.chat.id, "https://fanibani.ru/wp-content/uploads/2022/12/1638452060_132-celes-club-p-milii-kotenok-zhivotnie-krasivo-foto-138.jpg")
            break
        elif i == 13:
            bot.send_message(message.chat.id, "https://static.mk.ru/upload/entities/2023/05/17/03/articles/facebookPicture/b9/21/19/09/edbc7106048400a8f03c91c84c2205dd.jpg")
            break
        elif i == 14:
            bot.send_message(message.chat.id, "https://w.forfun.com/fetch/b3/b3f26a45b8b36be08b352477ff5f7dfc.jpeg")
            break
        elif i == 15:
            bot.send_message(message.chat.id, "https://pichold.ru/wp-content/uploads/2018/02/6b73f79f6b76456370a9cf20c6f892b7.jpg")
            break
        elif i == 16:
            bot.send_message(message.chat.id, "https://mykaleidoscope.ru/uploads/posts/2018-05/1527595731_foto_koshek__7285_-_sunray_-_pitomnik_britanskih_koshek.jpg")
            break
        elif i == 17:
            bot.send_message(message.chat.id, "https://kartinkin.net/uploads/posts/2022-02/1644933261_71-kartinkin-net-p-kartinki-milikh-kotikov-79.jpg")
            break
        elif i == 18:
            bot.send_message(message.chat.id, "https://damion.club/uploads/posts/2022-01/1642835541_83-damion-club-p-ochen-milie-kotyata-85.jpg")
            break
        elif i == 19:
            bot.send_message(message.chat.id, "https://wdorogu.ru/images/wp-content/uploads/2020/10/1527595801_kotenok_devochka_britanskaya_korotkosherstnaya_britanka_chernaya.jpg")
            break
        elif i == 20:
            bot.send_message(message.chat.id, "https://img.youscreen.ru/wall/14977113405599/14977113405599_1920x1200.jpg")
            break
        elif i == 21:
            bot.send_message(message.chat.id, "https://wdorogu.ru/images/wp-content/uploads/2020/10/2fdf2b2be1825b9.jpg")
            break
        elif i == 22:
            bot.send_message(message.chat.id, "https://damion.club/uploads/posts/2022-01/1642798564_11-damion-club-p-malenkii-milii-kotenok-11.jpg")
            break
        elif i == 23:
            bot.send_message(message.chat.id, "https://shutniks.com/wp-content/uploads/2019/11/milye_kotyata_i_smeshnye_32_30114121.jpg")
            break
@bot.message_handler(
    commands=['kalkul_matric', 'sinonimaizer', 'anti_copy_plagiat', 'free_IT_courses', 'best_kalkul', 'sleep_manager',
              'spargalka'])
def sites(message):
    if message.text == '/kalkul_matric':
        bot.send_message(message.chat.id,
                         '<a href="https://ru.onlinemschool.com/math/assistance/matrix/multiply/">kalkul_matric</a>',
                         parse_mode='html')
    elif message.text == '/sinonimaizer':
        bot.send_message(message.chat.id, '<a href="https://maxtext.ru/sinonimaizer-teksta-online">sinonimaizer</a>',
                         parse_mode='html')
    elif message.text == '/free_IT_courses':
        bot.send_message(message.chat.id, '<a href="https://stepik.org/catalog">free_IT_courses</a>', parse_mode='html')
    elif message.text == '/best_kalkul':
        bot.send_message(message.chat.id, '<a href="https://www.mathway.com/ru/Algebra">best_kalkul</a>',
                         parse_mode='html')
    elif message.text == '/anti_copy_plagiat':
        bot.send_message(message.chat.id, '<a href="https://text.ru/antiplagiat">anti_copy_plagiat</a>',
                         parse_mode='html')
    elif message.text == '/sleep_manager':
        bot.send_message(message.chat.id, '<a href="https://sleepytime.cc/">sleep_manager</a>', parse_mode='html')
    elif message.text == '/spargalka':
        bot.send_message(message.chat.id, '<a href="https://cheatography.com/">spargalka</a>', parse_mode='html')




@bot.message_handler(commands=['infa'])
def main(message):
    bot.send_message(message.chat.id,
                     'Это бот создан Sam1q, Allorin, cubikRUbik и Black_lenin. Надеемся, что функционал вам понравится!❤️')


@bot.message_handler(commands=['help'])
def start(message):
    bot.send_message(message.chat.id, 'Список моих команд:\n /start\n /sites\n /infa\n /haha\n')


@bot.message_handler(content_types=['photo'])
def start(message):
    file_path = bot.get_file(message.photo[-1].file_id).file_path
    file = bot.download_file(file_path)
    with open("./images/userPhoto.png", "wb") as code:
        code.write(file)
    create('./images/userPhoto.png')
    bot.send_photo(message.chat.id, open('./images/output.png', 'rb'), timeout=60)

while True:
    try:
        bot.polling(none_stop=True)
    except Exception as e:
        print(e)
