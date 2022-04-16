from pyexpat import model
from webbrowser import get
import django
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.generic import ListView
from .models import Post

# Create your views here.
def index(request):
    return render(request, 'index.html')

def post_list_view(request):
    return render(request, 'posts/post_list.html')

def post_detail_view(request, id):
    return render(request, 'posts/post_detail.html')

def post_create_view(request):
    return render(request, 'posts/post_form.html')

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