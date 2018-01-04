from django.middleware.common import MiddlewareMixin


class WeChatMiddleware(MiddlewareMixin):

    def process_request(self, request):
        pass

