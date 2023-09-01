import requests
from bs4 import BeautifulSoup
import re
import pandas as pd
import math

url = 'https://www.kabum.com.br/perifericos/teclado-mouse/teclado-sem-fio'

headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 \
           (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36'}

site = requests.get(url, headers=headers)
soup = BeautifulSoup(site.content, 'html.parser')

#Getting the total number of products
qtd_itens = soup.find('div', id = 'listingCount').get_text().strip()
#print(qtd_itens)
index = qtd_itens.find(' ')
#Iterating through the space to get just the number, without the word 'products'
qtd = qtd_itens[:index]
#print(qtd)

last_page = math.ceil(int(qtd) / 20)

dic_product = {'brand':[], 'price': []}

for page in range(1, last_page + 1):
    url_page = f'https://www.kabum.com.br/perifericos/teclado-mouse/teclado-sem-fio?page_number={page}&page_size=20&facet_filters=&sort=most_searched'
    site = requests.get(url_page, headers=headers)
    soup = BeautifulSoup(site.content, 'html.parser')

    products = soup.find_all('div', class_=re.compile('productCard'))

    for product in products:
        brand = product.find('span', class_=re.compile('nameCard')).get_text().strip()
        price = product.find('span', class_=re.compile('priceCard')).get_text().strip()

        print(brand, price)
    print(url_page)