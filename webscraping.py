import requests
from bs4 import BeautifulSoup
import time
from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

# web scraping
url = "https://simple.ripley.cl/tecno/computacion/notebooks?source=search&term=notebooks&s=mdco"
r = requests.get(url)
soup = BeautifulSoup(r.content, "html.parser")

catalogo = soup.find_all("div", {"class": "catalog-product-item"})

# bot de telegram
bot = Bot(token='5446917926:AAGNVWK7cjTyy5Zt4rq-YOyy_aYfdLC3bvs')
dp = Dispatcher(bot)

btn1 = InlineKeyboardButton(text='1 Producto', callback_data='uno')
btn2 = InlineKeyboardButton(text='3 Productos', callback_data='tres')
btn3 = InlineKeyboardButton(text='5 Productos', callback_data='cinco')
keyboard_inline = InlineKeyboardMarkup().add(btn1, btn2, btn3)


@dp.message_handler(commands=['ping'])
async def send_ping(message: types.Message):
    await message.reply("Toi vivo")


@dp.message_handler(commands=['producto'])
async def producto(message: types.Message):
    title = soup.find('div', {'class': 'catalog-product-details__name'}).text
    price = soup.find('li', {'class': 'catalog-prices__offer-price'}).text
    links = soup.find('a', {'class': 'catalog-product-item__container'}, href=True)
    await message.reply(
        "Mira esto: \n" + title + '\n' +
        f"  {'Solo a : ' + str(price)}\n" +
        'https://simple.ripley.cl' + links.get(
            'href'))


@dp.message_handler(commands=['productos'])
async def r_variosproductos(message: types.Message):
    await message.reply("¿Cuantos productos quieres ver?", reply_markup=keyboard_inline)


@dp.callback_query_handler(text=['uno', 'tres', 'cinco'])
async def variosproductos(call: types.CallbackQuery):
    if call.data == 'uno':
        time.sleep(0.3)
        title = soup.find('div', {'class': 'catalog-product-details__name'}).text
        price = soup.find('li', {'class': 'catalog-prices__offer-price'}).text
        links = soup.find('a', {'class': 'catalog-product-item__container'}, href=True)

        await call.message.answer(
            "Mira esto:\n" + title + '\n' +
            f"  {'Solo a : ' + str(price)}\n" +
             'https://simple.ripley.cl' + links.get(
                'href'))
    if call.data == 'tres':
        for i in range(3):
            time.sleep(0.3)
            title = soup.find('div', {'class': 'catalog-product-details__name'}).text
            price = soup.find('li', {'class': 'catalog-prices__offer-price'}).text
            links = soup.find('a', {'class': 'catalog-product-item__container'}, href=True)

            await call.message.answer(
                "Mira esto:\n" + title + '\n' +
                f"  {'Solo a : ' + str(price)}\n" +
                'https://simple.ripley.cl' + links.get(
                    'href'))
    if call.data == 'cinco':
        for i in range(5):
            time.sleep(0.3)
            title = soup.find('div', {'class': 'catalog-product-details__name'}).text
            price = soup.find('li', {'class': 'catalog-prices__offer-price'}).text
            links = soup.find('a', {'class': 'catalog-product-item__container'}, href=True)

            await call.message.answer(
                "Mira esto:\n" + title + '\n' +
                f"  {'Solo a : ' + str(price)}\n" +
                'https://simple.ripley.cl' + links.get(
                    'href'))


executor.start_polling(dp)
