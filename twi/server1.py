# -*- coding: utf-8 -*-
# Created by 0138695 on 2017/1/24

from twisted.internet.protocol import Protocol
from twisted.internet.protocol import  Factory
from twisted.internet import reactor

class TcpServerHandle(Protocol):
	def connectionMade(self):
		print "connectionMade"

	def connectionLost(self, reason):
		print "connectionLost"

	def dataReceived(self, data):
		print "dataRecived:",data
		self.transport.write("hello world")

factory = Factory()
factory.protocol = TcpServerHandle
reactor.listenTCP(8999,factory)
reactor.run()