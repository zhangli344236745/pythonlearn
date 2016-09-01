__author__ = '0138695'
from twisted.protocols.basic import LineOnlyReceiver
from twisted.internet.protocol import Factory
from twisted.internet import reactor

class TcpServerHandle(LineOnlyReceiver):
    def connectionMade(self):
        print("connectionMade")

    def connectionLost(self, reason):
        print("connectionLost")

    def lineReceived(self, line):
        print("lineR:",line)


factory = Factory()
factory.protocol = TcpServerHandle
reactor.listenTCP(8888,factory)
reactor.run()