# Create your views here.
from django.http import HttpResponse, JsonResponse
from django.views import View


class BookView(View):
    def get(self, requset, *args, **kwargs):
        return HttpResponse('get ~~~')

    # postman 请求需要将 CSRF 中间件屏蔽
    def post(self, request, *args, **kwargs):
        # 返回非 Json 格式，safe=False
        return JsonResponse({'date': 'post !!!'})
