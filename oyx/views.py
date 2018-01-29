import hashlib

from django.utils.encoding import smart_str
from django.shortcuts import HttpResponse
from django.views.generic.base import View
from django.views.decorators.csrf import csrf_exempt

from wechatpy import parse_message
from wechatpy.replies import TextReply

# Create your views here.


WEIXIN_TOKEN = '1996829wangjiu'
AppID = 'wx570b8fb034b12653'
AppSecret = '3e6c56c57e0a44fde641d14892f991a3'


class WeChatView(View):

    def get(self, request, *args, **kwargs):
        signature = request.GET.get("signature", None)
        timestamp = request.GET.get("timestamp", None)
        nonce = request.GET.get("nonce", None)
        echostr = request.GET.get("echostr", None)
        token = WEIXIN_TOKEN
        tmp_list = [token, timestamp, nonce]
        tmp_list.sort()
        tmp_str = "%s%s%s" % tuple(tmp_list)
        tmp_str = tmp_str.encode()
        tmp_str = hashlib.sha1(tmp_str).hexdigest()
        if tmp_str == signature:
            return HttpResponse(echostr)
        else:
            return HttpResponse("weixin  index")

    @csrf_exempt
    def post(self, request, *args, **kwargs):
        print(request.body)
        xml_str = smart_str(request.body)
        msg = parse_message(xml_str)
        reply = TextReply(content=msg.content, message=msg, type='text')
        xml = reply.render()
        return HttpResponse(xml)

