# -*- coding:utf-8 -*-
import socket
import os

HOST='127.0.0.1'
PORT=8888
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)      #定义socket类型，网络通信，TCP
s.connect((HOST,PORT))       #要连接的IP与端口
while True:
    cmd = "hello world\n"       #与人交互，输入命令
    print("hllo")
    s.send(cmd)
    data=s.recv(1024)     #把接收的数据定义为变量
    print data         #输出变量
s.close()