import grpc

from crpcs import clientService_pb2_grpc
from utils.loggingUtils import get_logger


class TTClient(object):

    def __init__(self, serverIP, serverPort=9876):
        self.logger = get_logger()
        self.logger.info('connect to {}:{}'.format(serverIP, serverPort))
        self.channel = grpc.insecure_channel('{}:{}'.format(serverIP, serverPort))
        self.stub = clientService_pb2_grpc.ClientServiceStub(self.channel)

    def shutdown(self):
        self.logger.info('Shutdown')
        self.channel.close()

    def get_stub(self):
        return self.stub

