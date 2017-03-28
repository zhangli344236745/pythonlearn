# -*- coding: utf-8 -*-
# Created by 0138695 on 2017/3/23
from locust import HttpLocust,TaskSet,task

class WebsiteTasks(TaskSet):
	def on_start(self):
		print("on start")

	@task
	def index(self):
		self.client.get("http://www.baidu.com")

class WebsiteUser(HttpLocust):
    task_set = WebsiteTasks
    min_wait = 5000
    max_wait = 15000