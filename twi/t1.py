__author__ = '0138695'
from twisted.internet import reactor

def hello():
    print("hello world")
reactor.callWhenRunning(hello)
reactor.callLater(3,hello)
reactor.run()