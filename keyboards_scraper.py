import requests
from bs4 import BeautifulSoup
import re
import pandas as pd

url = 'https://www.kabum.com.br/perifericos/teclado-mouse/teclado-sem-fio'

headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 \
           (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36'}

site = requests.get(url, headers=headers)
soup = BeautifulSoup(site.content, 'html.parser')