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
    i = r.randint(1, 36)
    if i == 1:
            bot.send_message(message.chat.id, "https://fanibani.ru/wp-content/uploads/2022/12/malysh-koshka.jpg")

    elif i == 2:
            bot.send_message(message.chat.id, "https://fanibani.ru/wp-content/uploads/2022/12/da51384eb809ea34ea211da5d6e26a03.jpg")

    elif i == 3:
            bot.send_message(message.chat.id, "https://get.pxhere.com/photo/sweet-kitten-cat-mammal-whiskers-vertebrate-babies-kittens-himalayan-persian-small-to-medium-sized-cats-cat-like-mammal-carnivoran-dog-breed-group-1074107.jpg")

    elif i == 4:
            bot.send_message(message.chat.id, "https://zabavnikplus.ru/wp-content/uploads/2/6/d/26d7b18ceaf454a250283fd50d77db1c.jpeg")

    elif i == 5:
            bot.send_message(message.chat.id, "https://images8.alphacoders.com/104/1049186.jpg")

    elif i == 6:
            bot.send_message(message.chat.id, "https://fanibani.ru/wp-content/uploads/2022/12/sweet-kitten-cat-mammal-nose-whiskers-an-scaled.jpg")

    elif i == 7:
            bot.send_message(message.chat.id, "https://ferma-biz.ru/wp-content/uploads/2022/08/scale_1200-2-1.jpg")

    elif i == 8:
            bot.send_message(message.chat.id, "https://fanibani.ru/wp-content/uploads/2022/12/malenkij-pushistyj-kot-nok-myaukaet.jpg")

    elif i == 9:
            bot.send_message(message.chat.id, "https://fikiwiki.com/uploads/posts/2022-02/1644827414_25-fikiwiki-com-p-kartinki-smeshnie-krasivie-i-milie-pro-kot-27.jpg")

    elif i == 10:
            bot.send_message(message.chat.id, "https://fanibani.ru/wp-content/uploads/2022/12/kotionok-9-6.jpg")

    elif i == 11:
            bot.send_message(message.chat.id, "https://fikiwiki.com/uploads/posts/2022-02/1644827438_37-fikiwiki-com-p-kartinki-smeshnie-krasivie-i-milie-pro-kot-39.jpg")

    elif i == 12:
            bot.send_message(message.chat.id, "https://fanibani.ru/wp-content/uploads/2022/12/1638452060_132-celes-club-p-milii-kotenok-zhivotnie-krasivo-foto-138.jpg")

    elif i == 13:
            bot.send_message(message.chat.id, "https://static.mk.ru/upload/entities/2023/05/17/03/articles/facebookPicture/b9/21/19/09/edbc7106048400a8f03c91c84c2205dd.jpg")

    elif i == 14:
            bot.send_message(message.chat.id, "https://w.forfun.com/fetch/b3/b3f26a45b8b36be08b352477ff5f7dfc.jpeg")

    elif i == 15:
            bot.send_message(message.chat.id, "https://pichold.ru/wp-content/uploads/2018/02/6b73f79f6b76456370a9cf20c6f892b7.jpg")

    elif i == 16:
            bot.send_message(message.chat.id, "https://mykaleidoscope.ru/uploads/posts/2018-05/1527595731_foto_koshek__7285_-_sunray_-_pitomnik_britanskih_koshek.jpg")

    elif i == 17:
            bot.send_message(message.chat.id, "https://kartinkin.net/uploads/posts/2022-02/1644933261_71-kartinkin-net-p-kartinki-milikh-kotikov-79.jpg")

    elif i == 18:
            bot.send_message(message.chat.id, "https://damion.club/uploads/posts/2022-01/1642835541_83-damion-club-p-ochen-milie-kotyata-85.jpg")

    elif i == 19:
            bot.send_message(message.chat.id, "https://wdorogu.ru/images/wp-content/uploads/2020/10/1527595801_kotenok_devochka_britanskaya_korotkosherstnaya_britanka_chernaya.jpg")

    elif i == 20:
            bot.send_message(message.chat.id, "https://img.youscreen.ru/wall/14977113405599/14977113405599_1920x1200.jpg")

    elif i == 21:
            bot.send_message(message.chat.id, "https://wdorogu.ru/images/wp-content/uploads/2020/10/2fdf2b2be1825b9.jpg")

    elif i == 22:
            bot.send_message(message.chat.id, "https://damion.club/uploads/posts/2022-01/1642798564_11-damion-club-p-malenkii-milii-kotenok-11.jpg")

    elif i == 23:
            bot.send_message(message.chat.id, "https://shutniks.com/wp-content/uploads/2019/11/milye_kotyata_i_smeshnye_32_30114121.jpg")

    elif i == 24:
            bot.send_message(message.chat.id, "https://i.pinimg.com/originals/16/76/44/1676446a31c6d4cdb3e1e8a10fa86644.jpg")

    elif i == 24:
            bot.send_message(message.chat.id, "http://pro-kotikov.ru/wp-content/uploads/2018/06/cute-exotic6.jpg")

    elif i == 25:
            bot.send_message(message.chat.id, "https://searchthisweb.com/wallpaper/cute-kittens_4288x2848_a4v3k.jpg")

    elif i == 26:
            bot.send_message(message.chat.id, "https://get.wallhere.com/photo/2048x1345-px-animal-cute-eye-kitten-1908333.jpg")

    elif i == 27:
            bot.send_message(message.chat.id, "https://webpulse.imgsmail.ru/imgpreview?key=pulse_cabinet-image-73d95ddc-4439-4984-9b32-40b01114d767&mb=webpulse")

    elif i == 28:
            bot.send_message(message.chat.id, "https://shutniks.com/wp-content/uploads/2019/11/milye_kotyata_i_smeshnye_32_30114121.jpg")

    elif i == 29:
            bot.send_message(message.chat.id, "https://wdorogu.ru/images/wp-content/uploads/2020/10/2fdf2b2be1825b9.jpg")

    elif i == 30:
            bot.send_message(message.chat.id, "https://wdorogu.ru/images/wp-content/uploads/2020/10/s1200-2-15.jpg")

    elif i == 31:
            bot.send_message(message.chat.id, "https://chudo-prirody.com/uploads/posts/2021-08/1628637595_122-p-kotyata-milie-foto-132.jpg")

    elif i == 32:
            bot.send_message(message.chat.id, "http://mobilmusic.ru/mfile/08/0a/90/1586458.jpg")

    elif i == 33:
            bot.send_message(message.chat.id, "https://celes.club/uploads/posts/2022-10/1666931823_14-celes-club-p-samie-milie-kotiki-v-mire-krasivo-14.jpg")

    elif i == 34:
            bot.send_message(message.chat.id, "https://android-obzor.com/wp-content/uploads/2022/03/nastol.jpg")

    elif i == 35:
            bot.send_message(message.chat.id, "https://chudo-prirody.com/uploads/posts/2021-08/1628761106_138-p-foto-kotyat-milikh-i-nyashnikh-142.jpg")

    elif i == 36:
            bot.send_message(message.chat.id, "https://img.desktopwallpapers.ru/animals/pics/wide/1920x1200/4c87fb310b3e56afc11dad6ca2d1934f.jpg")
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
    bot.send_message(message.chat.id, 'Список моих команд:\n /start\n /sites\n /infa\n /haha\n /kitten\n также я могу отрисовывать картинки, отправьте мне любое фото!')


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
