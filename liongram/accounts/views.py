from django.shortcuts import redirect, render
from .forms import UserSignupForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout

def signup_view(request) :
    # GET 요청 시 HTML 응답
    if request.method == 'GET' :
        form = UserSignupForm()
        context = {
            'form' : form
        }
        return render(request, 'accounts/signup.html', context)

    # Post 요청 시 데이터 확인 후 회원 생성
    else :
        form = UserSignupForm(request.POST)
        try :
            if form.is_valid :
                # 회원가입 처리
                instance = form.save()
                return redirect('index')

            else :
                # 인덱스
                return redirect('accounts:signup')

        except ValueError :
            message = '잘못된 입력입니다.'
            context = {
                'form' : form,
                # 'message' : message,
            }
            return render(request, 'accounts/signup.html', context)


def login_view(request) :
    # GET, POST 분리
    if request.method == 'GET' :
        # 로그인 HTML 응답
        return render(request, 'accounts/login.html', {'form' : AuthenticationForm()})

    else :
        form = AuthenticationForm(request, request.POST)
        # 데이터 유효성 검사
        if form.is_valid() :
            # 비즈니스 로직 처리 - 로그인 처리
            login(request, form.user_cache)
            return redirect('index')
        else :
            # 비즈니스 로직 처리 - 로그인 실패
            # 응답
            context = {
                'form' : form
            }
            return render(request, 'accounts/login.html', context)


        # username = request.POST.get('username')
        # if username == '' :
        #     pass
        # password = request.POST.get('password')
        # if password == '' :
        #     pass
        # pass # 응답

        # user = User.objects.get(username=username)