from asyncio.windows_events import NULL
from urllib.request import Request
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect, render
from django.http import HttpResponse
from demos import random_lotto

# Create your views here.
def calculator(request) :
    # return HttpResponse('oioi')
    # 데이터 입력
    num1 = request.GET.get('num1')
    num2 = request.GET.get('num2')
    operators = request.GET.get('operators')

    # print(f'request.__dict__ = {request.__dict__}')

    #계산
    if operators == '+' :
        result = int(num1) + int(num2)
    elif operators == '-' :
        result = int(num1) - int(num2)
    elif operators == '*' :
        result = int(num1) * int(num2)
    elif operators == '/' :
        result = int(num1) / int(num2)
    else :
        result = 0
    
    #응답
    return render(request, 'calculator.html', {'result' : result})


def lotto(request) :
    times = request.GET.get('times')
    lotto_list = []
    if times != None :
        for i in range(int(times)) :
            lotto_list.append(random_lotto.run())
        return render(request, 'lotto_result.html', {
            'times' : times,
            'lotto_list' : lotto_list
        })
    return render(request, 'lotto_intro.html')

# def lotto_result(request) :
#     #form 에서 받아온 데이터

#     return render(request, 'lotto_result.html')