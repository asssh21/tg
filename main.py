import telebot
from telebot import types


bot = telebot.TeleBot('5169779515:AAE1STcClE8c_2tiCRUqoHCO2qFw8CKZhSk')



@bot.message_handler(commands=['start'])
def text_message(message):
    bot.send_message(message.chat.id, 'Привет!')

@bot.message_handler(commands = ['url'])
def url(message):
    markup = types.InlineKeyboardMarkup()
    btn_my_site = types.InlineKeyboardButton(text='Группа', url='https://vk.com/club210267924')
    markup.add(btn_my_site)
    bot.send_message(message.chat.id, "Нажми на кнопку и перейди на наш сайт.", reply_markup=markup)

@bot.message_handler(commands=['photo'])
def text_message(message):
    photo = open("vladimir_putin.png", 'rb')
    bot.send_photo(message.chat_id, photo)

@bot.message_handler(commands=['help'])
def text_message(message):
    bot.send_message(message.chat.id, 'Чем вам помочь?')

@bot.message_handler(commands=['callback'])
def cmd_start(message):
    start_keyboard = types.InlineKeyboardMarkup()
    Test = types.InlineKeyboardButton(text='Test', callback_data='Test')  # callback_data - проще говоря id кнопки, по  которой мы будем вызывать её
    IT = types.InlineKeyboardButton(text=' IT', callback_data=' IT')
    start_keyboard.add(Test, IT)
    bot.send_message(message.chat.id, 'А вот и callback кнопки!', reply_markup=start_keyboard)

#Если получаем callback ответ с клавиатуры запускаем функцию answer_callback
@bot.callback_query_handler(func=lambda c:c.data)
def answer_callback(callback):
    if callback.data == ' IT': # а вот мы используем id кнопки !
        pass
    elif callback.data == 'Test':
        pass


bot.polling()