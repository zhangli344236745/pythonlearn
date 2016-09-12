__author__ = '0138695'
from __future__ import absolute_import
from thrift import Thrift
from thrift.transport import TSocket
from thrift.transport import TTransport
from thrift.protocol import TBinaryProtocol

from my.zl.demo import Hello
from my.zl.demo.ttypes import *

try:
    transport = TSocket.TSocket('127.0.0.1', 10086)
    transport = TTransport.TFramedTransport(transport)

    protocol = TBinaryProtocol.TBinaryProtocol(transport)
    client = Hello.Client(protocol)

    transport.open()
    msg = client.say("say")
    print msg
    transport.close()
except:
    print "err"