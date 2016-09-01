__author__ = '0138695'

from twisted.internet import reactor,task
import requests

def hello(name):
    print("hello world==>"+name)

def request_baidu():
    res = requests.get("http://www.baidu.com")
    print(res)
    return res

task1 = task.LoopingCall(hello,"ding")
task1.start(10)

reactor.callWhenRunning(hello,"yudhai")
reactor.callLater(3,hello,"yuyue")
reactor.callLater(5,request_baidu)
reactor.run()



