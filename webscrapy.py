import requests as rq
from bs4 import BeautifulSoup as bs

page=rq.get("https://www.whatsapp.com/")
page
soup=bs(page.content,'html.parser')
print(soup)
