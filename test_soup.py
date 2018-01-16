#!/usr/bin/python3.5
import urllib
from bs4 import BeautifulSoup

quote_page = 'http://finance.ua/ua/currency'

page = urllib.request.urlopen(quote_page)

soup = BeautifulSoup(page, 'html.parser')

name_box = soup.find('td', attrs={'class': 'c3'})

# print(list(soup.children))

print(name_box)


#TEST 4 GITHUB
