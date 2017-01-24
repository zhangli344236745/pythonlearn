# -*- coding: utf-8 -*-
# Created by 0138695 on 2017/1/24
from twisted.web import server,resource
from twisted.internet import reactor

class MainResource(resource.Resource):
	isLeaf = True
	def render_GET(self,request):
		name = request.args['name'][0]
		request.responseHeaders.addRawHeader("Content-Type", "text/html; charset=utf-8")
		return "<html><body>hello"+name+"</body></html>"

site = server.Site(MainResource())
reactor.listenTCP(8080, site)
reactor.run()