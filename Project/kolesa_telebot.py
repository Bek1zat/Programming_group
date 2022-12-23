import telebot
import time
from telebot import types


token_file = open('Project/token.txt','rt')
TOKEN = token_file.read()
token_file.close()

bot = telebot.TeleBot(TOKEN)

dict_of_models = {
'Toyota':['Camry','Land Cruiser Prado','Land Cruiser','RAV4','Corolla','Estima','Alphard'],
'Volkswagen':['Passat','Golf','Polo','Vento','Transporter','Jetta','Touareg','Tiguan']
}

list_of_locations = ['Алматы', "Астана"]
dict_of_conditions = {'Новые автомобили':'novye-avtomobili','Автомобили с пробегом':'avtomobili-s-probegom'}

MARK = None
MODEL = None
LOCATION = None
CAR_CONDITION = None
CAR_BODY = None

def create_keyboard(list_of_buttons):
    markup = types.ReplyKeyboardMarkup(resize_keyboard= True)
    for btn_text in list_of_buttons:
        btn = types.KeyboardButton(btn_text)
        markup.add(btn)
    return markup

def choose_model(message,mark):

    markup = create_keyboard(dict_of_models[mark])
    bot.send_message(message.chat.id,'Выберите модель автомобиля',reply_markup=markup)
def choose_location(message):
    markup = create_keyboard(list_of_locations)
    bot.send_message(message.chat.id,'Выберите местоположение автомобиля',reply_markup= markup)
def choose_condition(message):
    pass


@bot.message_handler(commands=['start','Start'])
def send_start_message(message):
    markup = create_keyboard(['Toyota','Volkswagen'])
    bot.send_message(message.chat.id,'Выберите марку автомобиля',reply_markup= markup)

@bot.message_handler(content_types=['text'])
def reply_to_all_message(message):
    for mark in dict_of_models.keys():
        if message.text == mark:
            global MARK
            MARK = mark
            choose_model(message,mark)
    if message.text in dict_of_models[MARK]:
        for model in dict_of_models[MARK]:
            if message.text == model:
                global MODEL
                MODEL = model
                choose_location(message)
    if message.text in list_of_locations:
        for city in list_of_locations:
            if message.text == city:
                global LOCATION
                LOCATION = city


while True:
    try:

        bot.infinity_polling(2)
    except Exception as er:
        print(er)
        time.sleep(2)    
        continue

token_file = open('Project/token.txt','rt',encoding='utf-8')
token = token_file.read()
token_file.close()

bot = telebot.TeleBot(token)
dict_of_models = {'Toyota': ['Camry', 'Land Cruiser Prado',' Land Cruiser','RAV4', 'Corolla', 'Estima', 'Alphard'],
'Volkswagen': ['Passat','Golf','Polo','Vento','Transporter','Jetta','Touareg','Tiguan'] }

def create_keyboard(list_of_buttons):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    for btn_text in list_of_buttons:
        btn = types.KeyboardButton(btn_text)
        markup.add(btn)
    return markup

def choose_model(message, mark):

    markup = create_keyboard(dict_of_models[mark])
    bot.send_message(message.chat.id, 'выберите модель авто', reply_markup=markup)

@bot.message_handler(commands= ['start','Start'])
def send_start_message(message):
    markup = create_keyboard(['Toyota','Volkswagen'])
    bot.send_message(message.chat.id, 'выберите марку авто', reply_markup=markup)

@bot.message_handler(content_types=['text'])
def reply_to_all_message(message):
    for model in dict_of_models.keys():
        if message.text == model:
            choose_model(message, model)

while True:
    try:
        bot.infinity_polling(2)
    except Exception as er:
        print(er)
        time.sleep(2)
        continue