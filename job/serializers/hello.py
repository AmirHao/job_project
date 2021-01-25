from django.http import HttpResponse


# Create your views here.


def hello(request): # noqa
    return HttpResponse('hi, biu biu biu ~~')
