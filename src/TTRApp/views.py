from django.http import HttpResponse, JsonResponse
from google.protobuf.json_format import MessageToDict

from TTF.settings import TOPTOY_IP, TOPTOY_RPCS_PORT
from rpcs.TTClient import TTClient
from spinnerTypes.utils_pb2 import Integer, Empty

rpcClient = TTClient(TOPTOY_IP, TOPTOY_RPCS_PORT)

def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def height(request):
    ret = rpcClient.get_stub().getHeight(Empty())
    return JsonResponse(MessageToDict(ret))
