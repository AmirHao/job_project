import json

from django.http import HttpResponse
import ast

# Create your views here.
from django.views import View


def hello(request):  # noqa
    return HttpResponse('hi, biu biu biu ~~')


class jisuan(View):
    def get(self, request):
        a = request.GET.get('a')
        b = request.GET.get('b')
        if not (a and b):
            raise ValueError('参数缺失')
        c = ast.literal_eval(a) / ast.literal_eval(b)
        return HttpResponse('{} / {}结果是：{}'.format(a, b, c))

    def post(self, request):
        data = request.body
        data = json.loads(data)
        a = data.get('a')
        b = data.get('b')
        if not (a and b):
            raise ValueError('参数缺失')
        c = a * b
        return HttpResponse('{} * {}结果是：{}'.format(a, b, c))
