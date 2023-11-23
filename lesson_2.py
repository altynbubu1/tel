import telebot
from telebot import types

bot = telebot.TeleBot('6957363899:AAH1Ln4Zsjbto3P2jVfpqn1oTXM3sHAPe3I')
# #############
#
# markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
# item1 = types.KeyboardButton('menu')
# item2 = types.KeyboardButton('zakaz')
# item3 = types.KeyboardButton('kontacty')
# markup.add(item1, item2, item3)
#
# @bot.message_handler(commands=['start'])
# def start(message):
#     bot.send_message(message.chat.id, "Выберите опцию:", reply_markup=markup)
#
# bot.polling()



###########
# markup = types.InlineKeyboardMarkup()
# item = types.InlineKeyboardButton("Перейти по ссылке", url="https://www.youtube.com/watch?v=yci475Vwc10")
# item_2 = types.InlineKeyboardButton("Перейти по ссылке", url="https://www.youtube.com/watch?v=eAL4w-CEe8A")
# markup.add(item, item_2)
#
# @bot.message_handler(commands=['start'])
# def start(message):
#     bot.send_message(message.chat.id, "Нажмите на кнопку для перехода по ссылке:", reply_markup=markup)
#
# bot.polling()


###########
# markup = types.InlineKeyboardMarkup()
# item1 = types.InlineKeyboardButton("Кнопка 1", callback_data="button1")
# item2 = types.InlineKeyboardButton("Кнопка 2", callback_data="button2")
# markup.add(item1, item2)
#
# @bot.callback_query_handler(func=lambda call: True)
# def handle_callback_query(call):
#     if call.data == "button1":
#         bot.send_message(call.message.chat.id, "Вы нажали на Кнопку 1")
#     elif call.data == "button2":
#         bot.send_message(call.message.chat.id, "Вы нажали на Кнопку 2")
#
# @bot.message_handler(commands=['start'])
# def start(message):
#     bot.send_message(message.chat.id, "Выберите опцию:", reply_markup=markup)
#
# bot.polling()

###########

# Обработчик команды /start
@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, "Привет! Я бот, который может отправлять фото и видео. Используй команды /photo и /video.")

# Обработчик команды /photo для отправки фото
@bot.message_handler(commands=['photo'])
def send_photo(message):
    chat_id = message.chat.id

    # Отправка фото из файла
    photo = open('./img/priroda.jpeg', 'rb')  # Замените 'photo.jpg' на путь к вашей фотографии
    bot.send_photo(chat_id, photo)

    photo = open('./img/priroda.jpeg', 'rb')  # Замените 'photo.jpg' на путь к вашей фотографии
    bot.send_photo(chat_id, photo)

# Обработчик команды /video для отправки видео
@bot.message_handler(commands=['video'])
def send_video(message):
    chat_id = message.chat.id

    # Отправка видео из файла
    video = open('./video/2023-11-02 16.10.15.mp4', 'rb')  # Замените 'video.mp4' на путь к вашему видео
    bot.send_video(chat_id, video)

# Запуск бота
bot.polling()


# Обработчик команды /send_link для отправки ссылки
@bot.message_handler(commands=['send_link'])
def send_link(message):
    chat_id = message.chat.id

    # Текст сообщения с HTML-разметкой, включая ссылку
    message_text = "Это ссылка на [Google](https://www.google.com/)."

    # Отправка сообщения с разметкой в формате HTML
    bot.send_message(chat_id, message_text, parse_mode='HTML')

# Запуск бота
bot.polling()



