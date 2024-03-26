import telebot
from telebot import types
from database import create_suggestions_table, save_suggestion


TOKEN = '7149432995:AAH9bJNiFqfIxtmXhcsXRGD-ABaouzVGQJQ'
my_chat_id = 855580393
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start_message(message):
    keyboard = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
    button1 = types.KeyboardButton(text="Все курсы")
    button2 = types.KeyboardButton(text="О нас")
    button3 = types.KeyboardButton(text="Записаться на курс")
    button4 = types.KeyboardButton(text="Отзывы о курсе")
    keyboard.add(button1, button2, button3, button4)
    bot.send_message(message.chat.id, 'Откройте для себя мир кондитерского искусства на нашем курсе кондитера! Учим созданию невероятных десертов и тортов от профессионалов индустрии. Превратите свою страсть в профессию, присоединяйтесь прямо сейчас! 🍰🎂 Запишитесь на курсы кондитера, где вас ждет насыщенная программа, обширная теоритическая и практическая часть.', reply_markup=keyboard)

create_suggestions_table()
@bot.message_handler(commands=['suggestions'])
def handle_suggestions(message):
    bot.send_message(message.chat.id, 'Чтобы записаться на курсы, пожалуйста, напишите номер телефона и ваше имя:')
    bot.register_next_step_handler(message, process_suggestion)

def process_suggestion(message):
    save_suggestion(my_chat_id, message.text)
    bot.send_message(message.chat.id, 'Спасибо, вы успешно записаны! Мы свяжемся с Вами')

def info_funk(message):
    keyboard = types.InlineKeyboardMarkup()
    url_button = types.InlineKeyboardButton(text="Хотите узнать больше о моих кулинарных приключениях? Подписывайтесь на мой Instagram: ", url="https://www.instagram.com/cakeschoolkz?igsh=MWxtNGx1MWdvcjIwMw==")
    keyboard.add(url_button)
    bot.send_message(message.chat.id, "Instagram аккаунт", reply_markup=keyboard)

def send_rec(message):
    bot.send_message(message.chat.id, '1. Современные пироги')
    bot.send_message(message.chat.id, '2. Macarons 2.0')
    bot.send_message(message.chat.id, '3. Сладкий стол')


@bot.message_handler(commands=['reviews'])
def handle_reviews(message):
    send_reviews_link(message)

def send_reviews_link(message):
    keyboard = types.InlineKeyboardMarkup()
    url_button = types.InlineKeyboardButton(text="Отзывы учеников", url="https://www.instagram.com/s/aGlnaGxpZ2h0OjE3OTg1MzY0NzMzMzY3NDY3?story_media_id=3201160503006305704&igsh=MWRpZTN2NGJuMXZ2Yw==")
    keyboard.add(url_button)
    bot.send_message(message.chat.id, "Вы можете посмотреть отзыв, перейдя по ссылке ниже:", reply_markup=keyboard)

@bot.message_handler(content_types=['text'])
def repeat_all_message(message):
    if message.text.lower() == 'о нас':
        info_funk(message)
    elif message.text.lower() == 'все курсы':
        send_rec(message)
    elif message.text.lower() == 'записаться на курс':
        handle_suggestions(message)
    elif message.text.lower() == 'отзывы о курсе':
        handle_reviews(message)
    elif message.text == '1':
        recipe_text = 'Программа курса "Современные пироги":\n🍰 19 видеоуроков, которые откроются вам на курсе:'
        photo_url = 'https://www.dropbox.com/scl/fi/0ewttness65xsrsqnf8ng/1.jpg?rlkey=1l2aglsmm1m311ngef9w1purf&dl=0'
        bot.send_photo(message.chat.id, photo=photo_url, caption=recipe_text)
    elif message.text == '2':
        recipe_text = 'Программа курса: теория и рецепты по приготовлению макарон:\n 21 видеоурок, которые откроются вам на курсе:'
        photo_url = 'https://www.dropbox.com/scl/fi/jkhiquuklsd4wigo4x7bw/2.jpg?rlkey=a7oiywgtt4kz942h0kvm3ntot&dl=0'
        bot.send_photo(message.chat.id, photo=photo_url, caption=recipe_text)
    elif message.text == '3':
        recipe_text = 'Программа курса «Сладкий стол»:\n Макарон, зефир, мармелад, маршмеллоу. Курс для новичков, с самых основ.'
        photo_url = 'https://www.dropbox.com/scl/fi/otc2pk6w5w8c7j0ns1bbf/3.jpg?rlkey=o73arimqzw4nq06ow4cdlchlg&dl=0'
        bot.send_photo(message.chat.id, photo=photo_url, caption=recipe_text)
    else:
        bot.send_message(message.chat.id, 'Неизвестная команда. Попробуйте еще раз.')


@bot.message_handler()
def on_message(message):
    bot.send_message(message.chat.id, text=message.text)


bot.infinity_polling()




