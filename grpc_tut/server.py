
from concurrent import futures
import time
import math
import logging

import grpc

import mail_pb2 as pb2
import mail_pb2_grpc as pb2_grpc


_ONE_DAY_IN_SECONDS = 60 * 60 * 24


class MailServicer(pb2_grpc.SendServiceServicer):
    def __init__(self):
        pass

    def SendMessage(self, request, context):
        _from = request._from
        content = request.content
        _tos = request._to
        res = [f"{_from.name} send a message to {_to.name}: {content}" for _to in _tos]
        return pb2.MailResult(content=res)


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=3))
    pb2_grpc.add_SendServiceServicer_to_server(MailServicer(), server)
    server.add_insecure_port('[::]:50051')
    server.start()

    try:
        while True:
            time.sleep(_ONE_DAY_IN_SECONDS)
    except KeyboardInterrupt:
        server.stop(0)


if __name__ == '__main__':
    logging.basicConfig()
    serve()

