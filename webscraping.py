import requests
from bs4 import BeautifulSoup
import telebot
# from webscraping import precioDeseado
# from webscraping import precioInicial
# from webscraping import price, title, links, catalogo
import requests
        

#web scraping
url = ("https://simple.ripley.cl/tecno/computacion/notebooks?source=search&term=notebooks&s=mdco")
r = requests.get(url)
soup = BeautifulSoup(r.content,"html.parser")
# links = soup.find_all('a',{'class': 'catalog-product-item'},href=True)

# for i in catalogo:
#     title  = i.find('div',{'class':'catalog-product-details__name'}).text
#     price = i.find('li',{'class':'catalog-prices__offer-price'}).text
# for href in soup.find_all('a',{'class': 'catalog-product-item'},href=True):
#     links = href.get('href')

bot = telebot.TeleBot('5446917926:AAGNVWK7cjTyy5Zt4rq-YOyy_aYfdLC3bvs')
catalogo = soup.find_all("div", {"class":"catalog-product-item"})

#bot de telegram
@bot.message_handler(commands=['producto'])
def pedirProducto(msg):
    title  = soup.find('div',{'class':'catalog-product-details__name'}).text
    price = soup.find('li',{'class':'catalog-prices__offer-price'}).text
    links = soup.find('a',{'class': 'catalog-product-item__container'}, href=True)
    bot.reply_to(msg,"Mira esto:\n" + title+ '\n' + f"  {'Solo a : '+str(price)}\n" + 'https://simple.ripley.cl' + links.get('href') )
    
@bot.message_handler(commands=['productos'])
def pedirProducto(msg):
    for i in catalogo:
        title  = i.find('div',{'class':'catalog-product-details__name'}).text
        price = i.find('li',{'class':'catalog-prices__offer-price'}).text
        links = i.find('a',{'class': 'catalog-product-item__container'}, href=True)

        bot.reply_to(msg,"Mira esto:\n" + title+ '\n' + f"  {'Solo a : '+str(price)}\n" + 'https://simple.ripley.cl' + links.get('href'))
     
        
   
    
bot.infinity_polling() 
 








# precioInicio_text = resultado.text.replace('$',' ')
# precioInicial = float(precioInicio_text)















# precioDeseado = 300000




# if precioInicial < precioDeseado:
#     print("No hay oferta")
# else:
#     print("Hay oferta")



