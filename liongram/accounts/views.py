from django.shortcuts import redirect, render
from .forms import UserSignupForm, UserUpdateForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required

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
        form = UserSignupForm(request.POST, request.FILES)
        try :
            if form.is_valid :
                # 회원가입 처리
                instance = form.save()
                context = {
                    "message" : "회원가입이 완료되었습니다.\n로그인해 주세요."
                }
                return render(request, 'index.html', context)

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

@login_required
def update_view(request) :
    # GET
    if request.method == 'GET' :
        context = {
            'form' : UserUpdateForm(instance = request.user) # 유저 정보를 인스턴스로 같이 넘김
        }
        return render(request, 'accounts/update.html', context)

    # POST
    else :
        form = UserUpdateForm(request.POST, request.FILES, instance = request.user)
        if form.is_valid() :
            form.save()
            return redirect('index')

@login_required
def logout_view(request) :
    # 데이터 유효성 검사
    if request.user.is_authenticated :
        # 비즈니스 로직 처리 - 로그아웃
        logout(request)
    
    # 응답
    return redirect('index')