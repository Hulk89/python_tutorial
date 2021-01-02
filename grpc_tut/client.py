
import random
import logging

import grpc

import mail_pb2 as pb2
import mail_pb2_grpc as pb2_grpc


def run():
    with grpc.insecure_channel('localhost:50051') as channel:
        stub = pb2_grpc.SendServiceStub(channel)
        msg = pb2.Mail(content="send it",
                       _from=pb2.Person(name="hulk", age=33, weight=84),
                       _to=[pb2.Person(name="bulk", age=10, weight=40),
                            pb2.Person(name="you", age=20, weight=50)])
        res = stub.SendMessage(msg)
        print(res.content)
        
if __name__ == '__main__':
    logging.basicConfig()
    run()
