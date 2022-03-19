from attr import attr
import requests
from bs4 import BeautifulSoup
import pandas as pd 

response = requests.get('https://lista.mercadolivre.com.br/placa-de-video')
print(response)

site = BeautifulSoup(response.text, 'html.parser')

products = site.findAll('div', attrs={'class': 'andes-card andes-card--flat andes-card--default ui-search-result ui-search-result--core andes-card--padding-default andes-card--animated'})

for product in products:
    
    title = product.find('h2', attrs={'class': 'ui-search-item__title ui-search-item__group__element'})
    #print(title.text)

    link = product.find('a', attrs={'class': 'ui-search-link'})
    #print(link['href'])

    price_fraction = product.find('span', attrs={'class': 'price-tag-fraction'})
    
    price_cents = product.find('span', attrs={'class': 'price-tag-cents'})

    if price_cents: 
        print(price_fraction.text + ',' + price_cents.text)
    else:
        print(price_fraction.text + ',' + ',00')
