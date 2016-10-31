__author__ = '0138695'
import scrapy
from bs4 import BeautifulSoup
from scrapy1.items import QuoteItem

class QuotesSpider(scrapy.Spider):
    name = 'quotes'

    start_urls = [
        'http://quotes.toscrape.com/page/1/',
    ]

    def parse(self, response):
        for quote in response.css("div.quote"):
            item = QuoteItem()
            item['text'] = quote.css('span.text::text').extract_first()
            item['author'] = quote.css('span small::text').extract_first()
            item['tags'] = quote.css('div.tags a.tag::text').extract()
            yield item
        next_page = response.css("li.next a::attr(href)").extract_first()
        if next_page is not None:
            next_page = response.urljoin(next_page)
            yield scrapy.Request(next_page, callback=self.parse)
        # body_soup = BeautifulSoup(response.body,"html.parser")
        # #print body_soup
        # objs = body_soup.find_all("div",attrs={'class':"quote"})
        # for obj in objs:
        #     #print obj
        #     text = obj.find("span",attrs={"text"}).string
        #     author = obj.select('span small')[0].string
        #     print(u'{}: {}'.format(author, text))
        #     item = QuoteItem()
        #     item['text'] = text
        #     item['author'] = author
        #     yield item


