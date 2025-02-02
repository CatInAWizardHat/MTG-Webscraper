import requests
from requests import get
from bs4 import BeautifulSoup
import pandas as pd
import numpy as np

card_name = input("Card name: ")


url = f"https://www.kanatacg.com/products/search?q={card_name}&c=1"
headers = {"Accept-Language": "en-US, en;q=0.5"}
results = requests.get(url, headers=headers)

soup = BeautifulSoup(results.text, "html.parser")

# initiate data storage
prices_nm = []
prices_vg = []
prices_ex = []
category_edition = []
in_stock = []


card_div = soup.find_all('form', class_='add-to-cart-form')

# our loop through each container
for container in card_div:
    print(container)
    # category/edition
    # edition = 