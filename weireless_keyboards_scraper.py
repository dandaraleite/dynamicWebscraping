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

