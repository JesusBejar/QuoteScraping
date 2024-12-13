from urllib import request
import requests
from bs4 import BeautifulSoup
from csv import writer
from time import sleep
from random import choice

# list to store scraped books
all_books = []

# constant part of url
base_url = 'http://books.toscrape.com'
# changing part of url
url = '/page/1'

