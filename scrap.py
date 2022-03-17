import requests
from bs4 import BeautifulSoup
import pandas as pd 

response = requests.get('http://books.toscrape.com/')

content = response.content

site = BeautifulSoup(content, 'html.parser')

list_infos = []

all_infos = site.findAll('article', attrs={'class': 'product_pod'})

for info in all_infos:
    
    price = info.find('p', attrs={'class': 'price_color'})

    title = info.find('h3')

    list_infos.append([title.text, price.text])

print(list_infos)