# Importing the required libraries
import os

from IPython.display import display
import requests
import pandas as pd
from bs4 import BeautifulSoup
from tabulate import tabulate


def create_dir():
    # Directory
    dir_ = "T-Shirts-women"
    # Parent Directory path
    parent_dir = os.path.dirname(os.path.realpath(__file__))
    # Path
    path = os.path.join(parent_dir, dir_)
    # os_mkdir(path)
    return path


# for idx in excelData.index:

# url = excelData['URL'][idx]
url = 'https://www.emag.ro/search/tricouri-dama/tricouri/c?ref=search_category_2'

# # Downloading contents of the web page
data = requests.get(url).text
soup = BeautifulSoup(data, 'html.parser')

i=0
for item in soup.find_all('img'):
    # print(item['src'])
    headers = {"User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:60.0) Gecko/20100101 Firefox/60.0",
               "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
               "Accept-Language": "en-US,en;q=0.9"
               }

    img_data = requests.get(url=item['src'], headers=headers).content
    with open('T-Shirts-women' + "/" + 'image_name' + i.__str__()+ '.png', 'wb') as handler:
        print(img_data)
        handler.write(img_data)
    i=i+1
