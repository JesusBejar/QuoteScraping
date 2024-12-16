from urllib import request
import requests
from bs4 import BeautifulSoup
from csv import writer
from time import sleep
from random import choice

# list to store scraped books
all_books = []

# constant part of url
base_url = 'https://books.toscrape.com/'
# changing part of url
url = 'catalogue/page-1.html'

while url:

    res = requests.get(f"{base_url}{url}")
    print(f'I am now scraping {base_url}{url}! beep beep boop boop ')
    soup = BeautifulSoup(res.text, 'html.parser')

    # class name found in html page
    books = soup.find_all("article", class_="product_pod")

    # Print the number of extracted elements
    print(f"Number of products found: {len(books)}")

    for book in books: 
        title_element = book.find("h3")
        if title_element:
            title = title_element.find("a").get_text() 

            price_element = book.find("p", class_="price_color")
            price = price_element.get_text() if price_element else "N/A"

            availability_element = book.find("p", class_="instock availability")
            availability = availability_element.get_text() if availability_element else "Unavailable"

            all_books.append({
                "title": title,
                "price": price,
                "availability": availability
            })

    next_btn = soup.find(_class='next')
    url = next_btn.find("a")["href"] if next_btn else None
    sleep(2)

    print("Here is some info about a certain book: ")
    book = choice(all_books)
    print(book)

    # try:
    #     stock_status = soup.find("p", class_="instock availability").get_text()
    #     print("stock info found")
    # except KeyError:
    #     stock_status = "Stock information not available"
    #     print(stock_status)

    print(book["title"])
    print(book["price"])
    print(book["availability"])
