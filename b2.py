__author__ = '0138695'
from bs4 import BeautifulSoup
markup = '<a href="http://example.com/">I linked to <i>example.com</i></a>'
soup = BeautifulSoup(markup,'html.parser')
tag = soup.a
tag.insert(2,"button")
print(tag.contents)
print(soup.a.contents)

soup2 = BeautifulSoup("<b>stop</b>","html.parser")
tag2 = soup2.new_tag("i")
tag2.string = "Dont"
soup2.b.string.insert_before(tag2)
print(soup2.b.contents)

