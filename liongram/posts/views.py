from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

# Create your views here.


def url_view(request):
    print('url_view()')
    # return HttpResponse('<h1>url_view')
    data = {'code' : '001', 'msg' : 'OK'}
    return JsonResponse(data)

# Data를 받는 방법
def url_prameter_view(request, username) :
    print('url_prameter_view()')
    print(username)
    print(request.GET)
    return HttpResponse(username)