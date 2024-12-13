from urllib import request
import requests
from bs4 import BeautifulSoup
from csv import writer
from time import sleep
from random import choice

# list to store scraped books
all_books = []

# constant part of url
base_url = 'http://books.toscrape.com/'
# changing part of url
url = '/page/1'

while url:

    res = requests.get(f"{base_url}{url}")
    print(f'I am now parsing {base_url}{url}! beep beep boop boop')
    soup = BeautifulSoup(res.text, 'html.parser')

    # class name found in html page
