import requests
from bs4 import BeautifulSoup
# import telebot
import time
from aiogram import Bot, Dispatcher, executor, types

bot = Bot(token='5446917926:AAGNVWK7cjTyy5Zt4rq-YOyy_aYfdLC3bvs')
dp = Dispatcher(bot)
        

# web scraping
url = "https://simple.ripley.cl/tecno/computacion/notebooks?source=search&term=notebooks&s=mdco"
r = requests.get(url)
soup = BeautifulSoup(r.content, "html.parser")
# links = soup.find_all('a',{'class': 'catalog-product-item'},href=True)

# for i in catalogo:
#     title  = i.find('div',{'class':'catalog-product-details__name'}).text
#     price = i.find('li',{'class':'catalog-prices__offer-price'}).text
# for href in soup.find_all('a',{'class': 'catalog-product-item'},href=True):
#     links = href.get('href')

#bot = telebot.TeleBot('5446917926:AAGNVWK7cjTyy5Zt4rq-YOyy_aYfdLC3bvs')
catalogo = soup.find_all("div", {"class": "catalog-product-item"})

# bot de telegram
@dp.message_handler(commands=['ping'])
async def send_ping(message: types.Message):
    await message.reply("Toi vivo")

@dp.message_handler(commands=['producto'])
async def pedirproducto(message: types.Message):
    title = soup.find('div', {'class': 'catalog-product-details__name'}).text
    price = soup.find('li', {'class': 'catalog-prices__offer-price'}).text
    links = soup.find('a', {'class': 'catalog-product-item__container'}, href=True)
    await message.reply("Mira esto: \n" + title + '\n' + f"  {'Solo a : '+str(price)}\n" + 'https://simple.ripley.cl' + links.get('href'))
    
@dp.message_handler(commands=['productos'])
async def pedirproductos(message: types.Message):
    cant = int(input("cuantos productos?"))
    for i in range(cant):
        time.sleep(0.3)
        title  = soup.find('div', {'class': 'catalog-product-details__name'}).text
        price = soup.find('li', {'class': 'catalog-prices__offer-price'}).text
        links = soup.find('a', {'class': 'catalog-product-item__container'}, href=True)

        await message.reply("Mira esto:\n" + title + '\n' + f"  {'Solo a : '+str(price)}\n" + 'https://simple.ripley.cl' + links.get('href'))
executor.start_polling(dp)
 








# precioInicio_text = resultado.text.replace('$',' ')
# precioInicial = float(precioInicio_text)















# precioDeseado = 300000




# if precioInicial < precioDeseado:
#     print("No hay oferta")
# else:
#     print("Hay oferta")



