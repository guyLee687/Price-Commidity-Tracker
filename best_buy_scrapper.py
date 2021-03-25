import os
import re
import requests 
from bs4 import BeautifulSoup

#This is a python comment 

URL = 'https://www.bestbuy.com/site/searchpage.jsp?_dyncharset=UTF-8&cp=3&id=pcat17071&iht=y&keys=keys&ks=960&list=n&sc=Global&st=gpu&type=page&usc=All%20Categories'
HEADER = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36'}
page = requests.get(URL, headers=HEADER)

#stores content of gpu
gpu_dict = {}

page_soup = BeautifulSoup(page.content, 'html.parser')

gpu_list = page_soup.find("ol", class_="sku-item-list")

for item in gpu_list.children: 
    if item["class"][0] != 'sku-item': 
        continue
    name = item.find("div", class_="sku-title")
    price = item.find("div", class_="price-block")
    gpu_dict[name.string] = price.find(string=re.compile("\\$"))

print(gpu_dict)