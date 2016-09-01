#client.py

#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys, glob, time,datetime
from my.test.demo import ClassMember
from my.test.demo.ttypes import *

from thrift import Thrift
from thrift.transport import TSocket
from thrift.transport import TTransport
from thrift.protocol import TBinaryProtocol

try:
  startTime = time.time()*1000
  # Make socket
  transport = TSocket.TSocket('127.0.0.1', 10086)

  # Framed is critical. Raw sockets are very slow
  transport = TTransport.TFramedTransport(transport)

  # Wrap in a protocol
  protocol = TBinaryProtocol.TBinaryProtocol(transport)

  # Create a client to use the protocol encoder
  client = ClassMember.Client(protocol)

  # Connect!
  transport.open()

  for i in range(1,6):
    i+=1
    s = Student()
    s.sid = i
    s.sname = "name_{}".format(i)
    r = client.Add(s)
    print(s)

  endTime = time.time()*1000

  print client.List(time.time()*1000)

  print "use:%d-%d=%dms" %(endTime,startTime, (endTime - startTime))
  print "name" ,(client.IsNameExist(time.time()*1000,"name_3"))
  # Close!
  transport.close()

except Thrift.TException, tx:
  print 'ERROR:%s' % (tx.message)
