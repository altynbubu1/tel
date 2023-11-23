import telebot
from telebot import types
# /cinema
bot = telebot.TeleBot('6970424156:AAHm9yQ15iLiBGjN7LZhaGSFX_PoYkregFk')

# Словарь для отслеживания состояний пользователя
user_states = {}


# Команда /start
@bot.message_handler(commands=['start'])
def welcome(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton('ANIME')
    item2 = types.KeyboardButton('МУЗЫКА')
    item3 = types.KeyboardButton('ФИЛЬМЫ')
    item4 = types.KeyboardButton('ИГРЫ')
    markup.add(item1, item2, item3, item4)
    bot.send_message(
        message.chat.id,
        f"Добро пожаловать, {message.from_user.first_name}!\nЯ - {bot.get_me().first_name}, бот созданный чтобы помогать вам.",
        parse_mode='html',
        reply_markup=markup
    )
    # Устанавливаем состояние пользователя в "start"
    user_states[message.chat.id] = "start"


# Обработка жанров фильмов
@bot.message_handler(func=lambda message: user_states.get(message.chat.id) == "start" and message.text == 'ФИЛЬМЫ')
def choose_movie_genre(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton('Детективы')
    item2 = types.KeyboardButton('Комедии')
    item3 = types.KeyboardButton('Ужасы')
    item4 = types.KeyboardButton('Назад')
    markup.add(item1, item2, item3, item4)
    bot.send_message(message.chat.id, 'Выберите жанр фильмов:', reply_markup=markup)
    # Устанавливаем состояние пользователя в "movie_genre"
    user_states[message.chat.id] = "movie_genre"


# Обработка жанров фильмов
@bot.message_handler(func=lambda message: user_states.get(message.chat.id) == "movie_genre")
def handle_movie_genre(message):
    if message.text == 'Детективы':
        bot.send_message(message.chat.id, 'Ссылка на детективы: https://www.ivi.ru/collections/50-best-detectives')
    elif message.text == 'Комедии':
        bot.send_message(message.chat.id, 'Ссылка на комедии: https://www.ivi.ru/movies/comedy/us')
    elif message.text == 'Ужасы':
        bot.send_message(message.chat.id, 'Ссылка на ужасы: https://www.ivi.ru/collections/scariest-horror-movies')
    elif message.text == 'Назад':
        # Вернуть пользователя в главное меню
        welcome(message)
    else:
        bot.send_message(message.chat.id, 'Пожалуйста, используйте клавиши на клавиатуре.')


# Обработка категории "ANIME"
@bot.message_handler(func=lambda message: user_states.get(message.chat.id) == "start" and message.text == 'ANIME')
def choose_anime_source(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton('JUTSU')
    item2 = types.KeyboardButton('ANIMEGO')
    item3 = types.KeyboardButton('Что такое аниме?')
    item4 = types.KeyboardButton('Назад')
    markup.add(item1, item2, item3, item4)
    bot.send_message(message.chat.id, 'Выберите через какой сайт будете смотреть аниме', reply_markup=markup)
    # Устанавливаем состояние пользователя в "anime_source"
    user_states[message.chat.id] = "anime_source"


# Обработка источника аниме
@bot.message_handler(func=lambda message: user_states.get(message.chat.id) == "anime_source")
def handle_anime_source(message):
    if message.text == 'JUTSU':
        bot.send_message(message.chat.id, 'Ссылка на JUTSU: https://www.jutsu.io/')
    elif message.text == 'ANIMEGO':
        bot.send_message(message.chat.id, 'Ссылка на ANIMEGO: https://animego.org/')
    elif message.text == 'Что такое аниме?':
        bot.send_message(message.chat.id, 'Аниме - это японская анимация.')
    elif message.text == 'Назад':
        # Вернуть пользователя в главное меню
        welcome(message)
    else:
        bot.send_message(message.chat.id, 'Пожалуйста, используйте клавиши на клавиатуре.')

if __name__ == "__main__":
    bot.polling(none_stop=True)
