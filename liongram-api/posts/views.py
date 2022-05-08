from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import api_view
from rest_framework.response import Response
from posts.serailizers import PostModelSerializer
from .models import Post

class PostModelViewSet(ModelViewSet) :
    queryset = Post.objects.all()
    serializer_class = PostModelSerializer


@api_view()
def calculator(reuqest) :
    # 1. 데이터 확인
    num1 = reuqest.GET.get('num1', 0)
    num2 = reuqest.GET.get('num2', 0)
    result = 0
    operators = reuqest.GET.get('operators')

    # 2. 계산
    if operators == '+' :
        result = int(num1) + int(num2)
    elif operators == '-' :
        result = int(num1) - int(num2)
    elif operators == '*' :
        result = int(num1) * int(num2)
    elif operators == '/' :
        result = int(num1) / int(num2)

    # 3. 응답
    data = {
        'type' : 'FBV',
        'result' : result,
    }

    return Response(data)