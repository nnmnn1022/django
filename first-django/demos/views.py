from urllib.request import Request
from django.http import HttpResponse
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def calculator(request) :
    # return HttpResponse('oioi')
    # 데이터 입력
    num1 = request.GET.get('num1')
    num2 = request.GET.get('num2')
    operators = request.GET.get('operators')

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