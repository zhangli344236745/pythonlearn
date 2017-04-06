# -*- coding: utf-8 -*-
# Created by 0138695 on 2017/4/6
import grpc
from example import data_pb2, data_pb2_grpc

_HOST = 'localhost'
_PORT = '8800'

def run():
    conn = grpc.insecure_channel(_HOST + ':' + _PORT)
    client = data_pb2_grpc.FormatDataStub(channel=conn)
    response = client.DoFormat(data_pb2.Data(text='hello,world!'))
    print("received: " + response.text)

if __name__ == '__main__':
    run()