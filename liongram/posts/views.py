from django.shortcuts import render, redirect, get_object_or_404 # 가져오거나 오류를 만든다
from django.http import Http404, HttpResponse, JsonResponse
from django.views.generic import ListView
from .models import Post
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from .forms import PostBaseForm, PostCreateForm, PostDetailForm
User = get_user_model()

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
    try :
        post = Post.objects.get(id=id)

    except Post.DoesNotExist:
        return redirect('index')
    context = {
        'post' : post,
        # 'form' : PostDetailForm(),
    }
    return render(request, 'posts/post_detail.html', context)

# 로그인을 했을 때만 처리하는 함수라는 어노테이션
@login_required
def post_create_view(request):
    # get으로 들어오면 폼을 보여주게 함
    if request.method == 'GET' :
        return render(request, 'posts/post_form.html')
    else :
        image = request.FILES.get('image')
        content = request.POST.get('content')
        Post.objects.create(
            image = image,
            content = content,
            writer = request.user
        )
        return redirect('index')


def post_create_form_view(request):
    # get으로 들어오면 폼을 보여주게 함
    if request.method == 'GET' :
        # 양식 제공
        form = PostCreateForm()
        context = {
            'form' : form
        }
        return render(request, 'posts/post_form_2.html', context)
    else :
        # 양식 제공이 아니라 값을 줘야되니까 Form에 데이터 넣어줌
        form = PostCreateForm(request.POST, request.FILES)
        
        # image = request.FILES.get('image')
        # content = request.POST.get('content')

        # 유효성 검사를 해서 form 기반 제대로된 정보인지 확인 후 데이터 저장
        if form.is_valid() :
            Post.objects.create(
                image = form.cleaned_data['image'],
                content = form.cleaned_data['content'],
                writer = request.user
            )
        else :
            return redirect('posts:post-create')
        return redirect('index')

    
@login_required
def post_update_view(request, id):
    # 아래 코드로 우측 코드를 대체할 수 있음 post = Post.objects.get(id=id)
    # 위 코드에서 does not exist Error가 났을 때 자동으로 404로 돌려주는 코드
    post = get_object_or_404(Post,id=id, writer=request.user)
    # if request.user != post.writer:
    #     raise Http404('잘못된 접근입니다.')
    if request.method == 'GET' :
        context = {
            'post' : post
        }
        return render(request, 'posts/post_form.html', context)
    elif request.method == 'POST':
        image = request.FILES.get('image')
        content = request.POST.get('content')

        if image :
            post.image.delete()
            post.image = image
        post.content = content
        post.save()
        return redirect('posts:post-detail', post.id )

@login_required
def post_delete_view(request, id):
    post = get_object_or_404(Post,id=id, writer=request.user)
    # if request.user != post.writer:
    #     raise Http404('잘못된 접근입니다.')
    if request.method == 'GET' :
        context = {
            'post' : post
        }
        return render(request, 'posts/post_confirm_delete.html', context)
    else :
        post.delete()
        return redirect('index')
    

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