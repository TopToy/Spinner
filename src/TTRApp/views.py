from django.http import HttpResponse, JsonResponse, HttpResponseBadRequest
from google.protobuf.json_format import MessageToDict
from rest_framework.decorators import api_view
from django.views.decorators.csrf import csrf_exempt

from rpcs.TTClient import TTClient
from settings import CORE_RPCS_PORT, CORE_IP
from spinnerTypes.client_pb2 import TxReq, BlockReq
from spinnerTypes.transaction_pb2 import Transaction
from spinnerTypes.utils_pb2 import Empty
from utils.jsonUtils import add_missing

rpcClient = TTClient(CORE_IP, CORE_RPCS_PORT)


def index(request):
    return HttpResponse("Hello, world. You're at the toptoy index.")


def height(request):
    ret = rpcClient.get_stub().getHeight(Empty())
    return JsonResponse(add_missing(ret, MessageToDict(ret)))


def liveness(request):
    rpcClient.get_stub().isAlive(Empty())
    return HttpResponse("server responses as expected")


def pool_size(request):
    ret = rpcClient.get_stub().poolSize(Empty())
    return JsonResponse(add_missing(ret, MessageToDict(ret)))


def pending_size(request):
    ret = rpcClient.get_stub().pendingSize(Empty())
    return JsonResponse(add_missing(ret, MessageToDict(ret)))


def validators(request):
    ret = rpcClient.get_stub().getValidators(Empty())
    return JsonResponse(add_missing(ret, MessageToDict(ret)))


def info(request):
    ret = rpcClient.get_stub().getConfigInfo(Empty())
    return JsonResponse(add_missing(ret, MessageToDict(ret)))


def tx_status(request, cid, worker, pid, bid, tx_num):
    req = TxReq()
    req.tid.channel = worker
    req.tid.proposerID = pid
    req.tid.bid = bid
    req.tid.txNum = tx_num
    req.blocking = bool(0)
    req.cid = cid
    ret = rpcClient.get_stub().txStatus(req)
    return JsonResponse(add_missing(ret, MessageToDict(ret)))


def read_tx(request, cid, worker, pid, bid, tx_num, blocking):
    req = TxReq()
    req.tid.channel = worker
    req.tid.proposerID = pid
    req.tid.bid = bid
    req.tid.txNum = tx_num
    req.blocking = bool(blocking)
    req.cid = cid
    ret = rpcClient.get_stub().readTx(req)
    return JsonResponse(add_missing(ret, MessageToDict(ret)))


def read_tx_data(request, cid, worker, pid, bid, tx_num, blocking):
    req = TxReq()
    req.tid.channel = worker
    req.tid.proposerID = pid
    req.tid.bid = bid
    req.tid.txNum = tx_num
    req.blocking = bool(blocking)
    req.cid = cid
    ret = rpcClient.get_stub().readTx(req)
    return JsonResponse({'data': str(ret.data, 'utf-8')})


def read_block(request, cid, height, blocking):
    req = BlockReq()
    req.height = height
    req.cid = cid
    req.blocking = bool(blocking)
    ret = rpcClient.get_stub().readBlock(req)
    return JsonResponse(add_missing(ret, MessageToDict(ret)))

@api_view(['POST'])
@csrf_exempt
def write_tx(request, cid):
    if request.method != 'POST':
        return HttpResponseBadRequest
    data = request.query_params['data']
    tx = Transaction()
    tx.clientID = cid
    tx.data = bytes(data, 'utf-8')
    ret = rpcClient.get_stub().writeTx(tx)
    return JsonResponse(add_missing(ret, MessageToDict(ret)))
