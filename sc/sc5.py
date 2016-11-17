# -*- coding:utf-8 -*-

from bs4 import BeautifulSoup
import requests
import re

headers = {
     'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.101 Safari/537.36',
}

url = "http://www.lotour.com/guoneiyou/"
web_data = requests.get(url,headers=headers)
print web_data.text
soup = BeautifulSoup(web_data.text,'lxml')
#imgs = soup.select("img")
# imgs = soup.find_all("img")
# for img in imgs:
#     print img

# titles = soup.select("div.auther > p > a")
# for title in titles:
#     print title

print soup.title.string
#print soup.find_all("p")
#
# for tag in soup.find_all(re.compile("p")):
#     print tag.get_text()

#print soup.find("a",class_="ltTqq")['title']
#print soup.find("a",class_="ltTqq")['title']
for item in soup.select("div.ltShare a"):
    print item["title"]
    print item.get_text()

print soup.select("div#ScrollLoadingDivID")[0].get_text()