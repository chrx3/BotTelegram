import telebot
# from webscraping import precioDeseado
# from webscraping import precioInicial
from webscraping import price, title, links, catalogo
import requests
bot = telebot.TeleBot('5446917926:AAGNVWK7cjTyy5Zt4rq-YOyy_aYfdLC3bvs')

# bot de telegram
@bot.message_handler(commands=['producto'])
def pedirProducto(msg):
    bot.reply_to(msg,"Mira esto:\n" + title+ '\n' + f"  {'Solo a : '+str(price)}\n" + 'https://simple.ripley.cl' + links )
    
@bot.message_handler(commands=['productos'])
def pedirProducto(msg):
    for i in catalogo:
        bot.reply_to(msg,[price])
        

    # bot.reply_to(msg,"Mira esto:\n" + title+ '\n' + f"  {'Solo a : '+str(price)}\n" + 'https://simple.ripley.cl' + links )
       

# telegram_bot_sendtext("Mira esto:\n" + title+ '\n' + f"  {'Solo a : '+str(price)}\n" + 'https://simple.ripley.cl' + links )

# if price == price:
#     test = telegram_bot_sendtext('hola')

# else:
#     test = telegram_bot_sendtext("No hay oferta")


# @bot.message_handler(commands=['start', 'help'])
# def send_welcome(message):
# 	bot.reply_to(message, "Wena por fin funcioan esta cosa")

# @bot.message_handler(func=lambda message: True)
# def echo_all(message):
# 	bot.reply_to(message, message.text)
# bot_token = '5446917926:AAGNVWK7cjTyy5Zt4rq-YOyy_aYfdLC3bvs'
#     bot_chatID = '969058692'
#     send_text = 'https://api.telegram.org/bot' + bot_token + '/sendMessage?chat_id=' + bot_chatID + '&parse_mode=Markdown&text=' + bot_message

#     response = requests.get(send_text)
    
#     return response.json()

bot.infinity_polling()   