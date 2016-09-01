__author__ = '0138695'
from bs4 import BeautifulSoup

soup = BeautifulSoup('<b class="bloaest">extream blod </b>','html.parser')
tag = soup.b
print(tag.name)
print(tag['class'])
tag['id'] = 3
print(tag)

markup = '<a href="http://example.com/">I linked to <i>example.com</i></a>'
soup2 = BeautifulSoup(markup,'html.parser')
soup2.prettify()
print(soup2.get_text())


html_doc = """
<html><head><title>The Dormouse's story</title></head>

<p class="title"><b>The Dormouse's story</b></p>

<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>

<p class="story">44444</p>
</body>
</html>
"""
soup4 = BeautifulSoup(html_doc,"html.parser")
print(soup4.find_all(id="link1"))
print(soup4.find_all("a",class_="sister"))
tag = soup4.title
print(tag.parent)
print(soup4.p)