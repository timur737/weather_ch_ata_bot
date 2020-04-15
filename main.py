import telebot
import requests
from bs4 import BeautifulSoup

token = '1288389478:AAHH74kqkbiypzhEhLwSvUVuP10HxTCroVg'

bot = telebot.TeleBot(token)



response = requests.get("https://api.openweathermap.org/data/2.5/weather",
                        params={
                            'q': 'Cholpon-Ata',
                            'APPID': 'e9d3276af5f63dadb4a1145429861381',
                            'mode': 'xml', 'units': 'metric', 'lang': 'ru'
                        })
soup = BeautifulSoup(response.content, 'xml')
keyboard1 = telebot.types.ReplyKeyboardMarkup()
keyboard1.row('Узнать погоду')


@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, soup.temperature['value'] + ' градусов целсия')
    bot.send_message(message.chat.id, soup.weather['value'])


@bot.message_handler(commands=['weather'])
def weather(message):
    bot.send_message(message.chat.id, soup.temperature['value'] + ' градусов целсия')
    bot.send_message(message.chat.id, soup.weather['value'])


@bot.message_handler(content_types=['text'])
def handle(message):
    if message.text == "Погода":
        bot.send_message(message.chat.id, soup.temperature['value'] + ' градусов целсия')
        bot.send_message(message.chat.id, soup.weather['value'])

bot.polling(none_stop=True)
