__author__ = '0138695'
import scrapy
from bs4 import BeautifulSoup

class MySpider(scrapy.Spider):
    name = 'cnblogs'
    allowed_domains = ['cnblogs.com']
    start_urls = [
        'http://www.cnblogs.com'
    ]

    def parse(self, response):
        html_soup = BeautifulSoup(response.body,"html.parser")
        for a in html_soup.find_all("a",attrs={"class":'titlelnk'}):
            yield {"title": a.string}

        for a in html_soup.find_all("a",attrs={"class":'titlelnk'}):
            print("zhangli",a["href"])
            yield scrapy.Request(a["href"], callback=self.parse)

        #for url in html_soup.find_all('//a/@href').extract():
            #yield scrapy.Request(url, callback=self.parse)