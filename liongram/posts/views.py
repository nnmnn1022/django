from email.mime import image
from pyexpat import model
from webbrowser import get
import django
from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from django.views.generic import ListView
from .models import Post, User
from django.contrib.auth.decorators import login_required

# Create your views here.
def index(request):
    post_list = Post.objects.all().order_by('-created_at')
    context = {
        'post_list' : post_list,
    }
    return render(request, 'index.html', context)

def post_list_view(request):
    post_list = Post.objects.all()
    # Post.writer가 현재 로그인인 것만 조회
    # post_list = Post.objects.filter(writer=request.user)
    # render 함수의 3번째 인자가 context(딕셔너리)이기 때문에 코딩할 때도 웬만하면 규칙을 지켜서 진행
    context = {
        'post_list' : post_list,
    }
    return render(request, 'posts/post_list.html', context)

def post_detail_view(request, id):
    return render(request, 'posts/post_detail.html')

# 로그인을 했을 때만 처리하는 함수라는 어노테이션
@login_required
def post_create_view(request):
    # get으로 들어온 것만 폼을 보여주게 함
    if request.method == 'GET' :
        return render(request, 'posts/post_form.html')
    else :
        image = request.FILES.get('image')
        content = request.POST.get('content')
        print(image)
        print(content)
        Post.objects.create(
            image = image,
            content = content,
            writer = request.user
        )
        return redirect('index')

    

def post_update_view(request, id):
    return render(request, 'posts/post_form.html')

def post_delete_view(request, id):
    return render(request, 'posts/post_confirm_delete.html')

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

def function_view(request) :
    print(f'request.method : {request.method}')
    if (request.method == 'GET') :
        print(f'request.method : {request.GET}')
    if (request.method == 'POST') :
        print(f'request.method : {request.POST}')
    return render(request, 'view.html')


class class_view(ListView):
    model = Post
    template_name = 'cbv_view.html'

def function_list_view(request) :
    object_list = Post.objects.all().order_by('-id')

    return render(request, 'cbv_view.html', {'object_list' : object_list})