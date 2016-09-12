# -*- coding:utf-8 -*-
import requests
from bs4 import BeautifulSoup

soup = BeautifulSoup("<html><head><title>ff</title></head><body><p>dat1</p><p>dat2</p></body></html>","html.parser")
print soup
print soup('p')

html = requests.get("http://www.jianshu.com").content

soup2 = BeautifulSoup(html,'html.parser',from_encoding="utf-8")
#print soup2
result = soup2('div')
print result

tags = soup2.find_all("a",attrs={"class":"btn"})
for tag in tags:
    print tag.i


