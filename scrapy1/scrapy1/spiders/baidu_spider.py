__author__ = '0138695'
import scrapy

class BaiduSpider(scrapy.Spider):
    name = "baidu"
    allowed_domains = ['baidu.com']
    start_urls = [
        "http://www.baidu.com"
    ]

    def parse(self, response):
        self.logger.info('A response from %s just arrived!', response.url)