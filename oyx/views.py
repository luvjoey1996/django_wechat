import hashlib

from django.shortcuts import HttpResponse
from django.views.generic.base import View
from django.views.decorators.csrf import csrf_exempt

# Create your views here.


WEIXIN_TOKEN = '1996829wangjiu'


class WeChatView(View):

    @csrf_exempt
    def get(self, request, *args, **kwargs):
        signature = request.GET.get("signature", None)
        timestamp = request.GET.get("timestamp", None)
        nonce = request.GET.get("nonce", None)
        echostr = request.GET.get("echostr", None)
        token = WEIXIN_TOKEN
        tmp_list = [token, timestamp, nonce]
        tmp_list.sort()
        tmp_str = "%s%s%s" % tuple(tmp_list)
        tmp_str = hashlib.sha1(tmp_str).hexdigest()
        if tmp_str == signature:
            return HttpResponse(echostr)
        else:
            return HttpResponse("weixin  index")

    def post(self, request, *args, **kwargs):
        pass
