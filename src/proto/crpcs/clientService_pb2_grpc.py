# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

from spinnerTypes import block_pb2 as spinnerTypes_dot_block__pb2
from spinnerTypes import client_pb2 as spinnerTypes_dot_client__pb2
from spinnerTypes import transaction_pb2 as spinnerTypes_dot_transaction__pb2
from spinnerTypes import utils_pb2 as spinnerTypes_dot_utils__pb2


class ClientServiceStub(object):
  # missing associated documentation comment in .proto file
  pass

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.writeTx = channel.unary_unary(
        '/proto.crpcs.clientService.ClientService/writeTx',
        request_serializer=spinnerTypes_dot_transaction__pb2.Transaction.SerializeToString,
        response_deserializer=spinnerTypes_dot_transaction__pb2.TxID.FromString,
        )
    self.readTx = channel.unary_unary(
        '/proto.crpcs.clientService.ClientService/readTx',
        request_serializer=spinnerTypes_dot_client__pb2.TxReq.SerializeToString,
        response_deserializer=spinnerTypes_dot_transaction__pb2.Transaction.FromString,
        )
    self.txStatus = channel.unary_unary(
        '/proto.crpcs.clientService.ClientService/txStatus',
        request_serializer=spinnerTypes_dot_client__pb2.TxReq.SerializeToString,
        response_deserializer=spinnerTypes_dot_client__pb2.TxStatus.FromString,
        )
    self.readBlock = channel.unary_unary(
        '/proto.crpcs.clientService.ClientService/readBlock',
        request_serializer=spinnerTypes_dot_client__pb2.BlockReq.SerializeToString,
        response_deserializer=spinnerTypes_dot_block__pb2.Block.FromString,
        )
    self.getHeight = channel.unary_unary(
        '/proto.crpcs.clientService.ClientService/getHeight',
        request_serializer=spinnerTypes_dot_utils__pb2.Empty.SerializeToString,
        response_deserializer=spinnerTypes_dot_utils__pb2.Integer.FromString,
        )
    self.isAlive = channel.unary_unary(
        '/proto.crpcs.clientService.ClientService/isAlive',
        request_serializer=spinnerTypes_dot_utils__pb2.Empty.SerializeToString,
        response_deserializer=spinnerTypes_dot_utils__pb2.Empty.FromString,
        )
    self.poolSize = channel.unary_unary(
        '/proto.crpcs.clientService.ClientService/poolSize',
        request_serializer=spinnerTypes_dot_utils__pb2.Empty.SerializeToString,
        response_deserializer=spinnerTypes_dot_utils__pb2.Integer.FromString,
        )
    self.pendingSize = channel.unary_unary(
        '/proto.crpcs.clientService.ClientService/pendingSize',
        request_serializer=spinnerTypes_dot_utils__pb2.Empty.SerializeToString,
        response_deserializer=spinnerTypes_dot_utils__pb2.Integer.FromString,
        )
    self.getValidators = channel.unary_unary(
        '/proto.crpcs.clientService.ClientService/getValidators',
        request_serializer=spinnerTypes_dot_utils__pb2.Empty.SerializeToString,
        response_deserializer=spinnerTypes_dot_client__pb2.Validators.FromString,
        )
    self.getConfigInfo = channel.unary_unary(
        '/proto.crpcs.clientService.ClientService/getConfigInfo',
        request_serializer=spinnerTypes_dot_utils__pb2.Empty.SerializeToString,
        response_deserializer=spinnerTypes_dot_client__pb2.ConfigInfo.FromString,
        )


class ClientServiceServicer(object):
  # missing associated documentation comment in .proto file
  pass

  def writeTx(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def readTx(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def txStatus(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def readBlock(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def getHeight(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def isAlive(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def poolSize(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def pendingSize(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def getValidators(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def getConfigInfo(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_ClientServiceServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'writeTx': grpc.unary_unary_rpc_method_handler(
          servicer.writeTx,
          request_deserializer=spinnerTypes_dot_transaction__pb2.Transaction.FromString,
          response_serializer=spinnerTypes_dot_transaction__pb2.TxID.SerializeToString,
      ),
      'readTx': grpc.unary_unary_rpc_method_handler(
          servicer.readTx,
          request_deserializer=spinnerTypes_dot_client__pb2.TxReq.FromString,
          response_serializer=spinnerTypes_dot_transaction__pb2.Transaction.SerializeToString,
      ),
      'txStatus': grpc.unary_unary_rpc_method_handler(
          servicer.txStatus,
          request_deserializer=spinnerTypes_dot_client__pb2.TxReq.FromString,
          response_serializer=spinnerTypes_dot_client__pb2.TxStatus.SerializeToString,
      ),
      'readBlock': grpc.unary_unary_rpc_method_handler(
          servicer.readBlock,
          request_deserializer=spinnerTypes_dot_client__pb2.BlockReq.FromString,
          response_serializer=spinnerTypes_dot_block__pb2.Block.SerializeToString,
      ),
      'getHeight': grpc.unary_unary_rpc_method_handler(
          servicer.getHeight,
          request_deserializer=spinnerTypes_dot_utils__pb2.Empty.FromString,
          response_serializer=spinnerTypes_dot_utils__pb2.Integer.SerializeToString,
      ),
      'isAlive': grpc.unary_unary_rpc_method_handler(
          servicer.isAlive,
          request_deserializer=spinnerTypes_dot_utils__pb2.Empty.FromString,
          response_serializer=spinnerTypes_dot_utils__pb2.Empty.SerializeToString,
      ),
      'poolSize': grpc.unary_unary_rpc_method_handler(
          servicer.poolSize,
          request_deserializer=spinnerTypes_dot_utils__pb2.Empty.FromString,
          response_serializer=spinnerTypes_dot_utils__pb2.Integer.SerializeToString,
      ),
      'pendingSize': grpc.unary_unary_rpc_method_handler(
          servicer.pendingSize,
          request_deserializer=spinnerTypes_dot_utils__pb2.Empty.FromString,
          response_serializer=spinnerTypes_dot_utils__pb2.Integer.SerializeToString,
      ),
      'getValidators': grpc.unary_unary_rpc_method_handler(
          servicer.getValidators,
          request_deserializer=spinnerTypes_dot_utils__pb2.Empty.FromString,
          response_serializer=spinnerTypes_dot_client__pb2.Validators.SerializeToString,
      ),
      'getConfigInfo': grpc.unary_unary_rpc_method_handler(
          servicer.getConfigInfo,
          request_deserializer=spinnerTypes_dot_utils__pb2.Empty.FromString,
          response_serializer=spinnerTypes_dot_client__pb2.ConfigInfo.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'proto.crpcs.clientService.ClientService', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))