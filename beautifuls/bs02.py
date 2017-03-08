# -*- coding: utf-8 -*-
# Created by 0138695 on 2017/3/8
import requests
from bs4 import BeautifulSoup

url = 'http://www.jianshu.com/users/845cc15feda3/timeline'
header = {'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:36.0) Gecko/20100101 Firefox/36.0'}

response = requests.get(url,headers=header)
html = response.text
#print html

soup = BeautifulSoup(html,'html.parser')
author_info = soup.find_all('div',class_="info")
infos =  soup.select("div.meta-block a")
for info in infos:
	print info.p.string
	print info.get_text()