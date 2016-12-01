# -*- coding:utf-8 -*-

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

brower = webdriver.Firefox()
brower.get("http://www.tianyancha.com")
search_input = brower.find_element_by_id("live-search")
search_input.send_keys(u"星巴克")
search_input.send_keys(Keys.ENTER)

