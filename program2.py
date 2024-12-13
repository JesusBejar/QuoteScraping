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
    books_on_page = soup.find_all(class_='product_pod')

    for book in books_on_page:
        all_books.append({
			'title': book.find(title_='').get_text(),
            'stock': book.find(class_='instock availability').get_text(),
			'price': book.find(class_='price_color').get_text()
        })
    next_btn = soup.find(_class='next')
    url = next_btn.find("a")["href"] if next_btn else None
    sleep(2)

    book = choice(all_books)
    print("Here is some book info: ")
    print(book["title"])
    print(book["stock"])
    print(book["price_color"])