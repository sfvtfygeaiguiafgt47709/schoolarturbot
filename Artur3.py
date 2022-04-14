from email import message
import telebot
from telebot import types

bot = telebot.TeleBot('5175734013:AAE8N4JLkXOoNDwOi7QkHOBn32qAzo6OSII')

@bot.message_handler(commands=['start'])
def start(message):
    mess = f'Hello,{message.from_user.first_name} {message.from_user.last_name}'
    bot.send_message(message.chat.id, mess, parse_mode = ['html'])

# @bot.message_handler()
# def get_user_text(message):
#    if message.text == 'Hello':
#       bot.send_message(message.chat.id, 'И тебе тоже привет', parse_mode = ['html'])
#    elif message.text =='id':
#       bot.send_message(message.chat.id, f'твой id{message.from_user.id}', parse_mode = ['html'])
#    elif message.text == 'photo':
#        photo = open('babule.png', 'rd')
#        bot.send_photo(message.chat.id, photo)
#    else:
#        bot.send_message(message.chat.id,'Я тебя не понимаю!', parse_mode = ['html'])

@bot.message_handler(content_types=['photo'])
def get_user_photo(message):
  bot.send_message(message.chft.id, 'Супер фото!')

@bot. message_handler(commands=['website'])
def webSite(message):
  markup = types.InlineKeyboardMarkup()
  markup.add(types.InlineKeyboardButton('WebSite', url='https://www.youtube.com/')) 
  bot.send_message(message.chat.id, 'WebSite', reply_markup=markup)

@bot. message_handler(commands=['help'])
def help(message):
  markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
  start = types.KeyboardButton('start')
  website = types.KeyboardButton('website')
  markup.add(start, website)
  bot.send_message(message.chat.id, 'Ок', reply_markup=markup)

bot.polling(none_stop = True)
