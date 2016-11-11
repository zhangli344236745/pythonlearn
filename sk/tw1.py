__author__ = '0138695'
from twisted.internet.protocol import Protocol,ServerFactory

HOST = "127.0.0.1"
PORT = 3000

class EchoProtocol(Protocol):
    def dataReceived(self, data):
        self.transport.write(data)
        print "data"

if __name__ == "__main__":
    factory = ServerFactory()
    factory.protocol = EchoProtocol

    from twisted.internet import reactor
    reactor.listenTCP(PORT, factory, interface=HOST)
    reactor.run()