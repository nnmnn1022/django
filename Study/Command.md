### 가상환경 설정
---
```
python -m  venv venv(이름)
pip install --upgrade pip
```

---

## Django
---
##### 프로젝트 생성
`django-admin startproject config .`


##### 앱 생성 (앱은 복수형으로 만들어야 해서 posts)
`django-admin startapp __your_app_name__`


##### app을 추가하면 반드시 해야 하는 일
`config/settings.py > INSTTALLED_APPS`에 app 명을 그대로 추가

##### manager.py 실행 (서버 실행)
`python manage.py runserver`

##### migrations
###### models에 데이터 베이스에 입력할 컬럼들을 명세 후

`python manage.py makemigrations`
모델 생성이나 변경 후 마이그레이트 준비

`python manage.py migrate`
준비 후 마이그레이션 실행

---
##### 관리자 만들기
`python manage.py createsuperuser`



---
### Models
---
##### 
> models > verbose_name은 admin 사용자에게 보여지는 이름



django superuser id : admin / 12

for _ in range(7) >>>> 변수 값에 _를 넣으면 변수를 사용하지 않겠다는 의미

templates 폴더를 앱 안에 넣어서 사용하는 것이 아니라 더 윗단에서 관리하는 방법 :
settings 안에 TEMPALATES 리스트가 있음 거기에 BASE_DIR / 'templates'를 넣을 것
templates 폴더 안에는 앱명으로 폴더를 하나 생성한 후 html 파일을 넣을 것

활용법 : veiws 안에서 render 할 때 (세팅에서 template 경로를 설정하였으니 templates 다음
앱 명/html파일명 형식으로 작성

앱 안에 url을 정리하는 파일을 만듦
urls.py를 만들고 상위에 있는 urls.py처럼 모두 추가한다. (urlpatterns)
프로젝트의 urls.py에
from django.urls import include
path('앱명/', include('앱명.urls')
두 줄  코드 삽입

04/21
이미지를 html form 태그로 보낼 때는 인코딩이 필요함
데이터를 어떤 형식으로 보낼 것인지에 대한 내용
enctype="multipart/form-data"

settings.py
Static : 서버에서 업로드
media : 사용자들이 업로드

settings의 내용을 가져오는 코드
from django.conf import settings

장고 디버그 툴바
https://django-debug-toolbar.readthedocs.io/en/latest/

05/01
custom user model을 사용하고자 할 때는
settings.py에 AUTH_USER_MODEL = '앱이름.앱에서 설정한 변수이름' 추가가 필요하다.
migrate 오류 시에 db를 삭제하는 것 외에 해결 방법은 없는지 확인 필요.

>> user를 커스터마이징 하는 방법 중에는 확장하는 방법도 있음

model을 하면 빼놓을 수 없는 manager,
쿼리셋 api를 저장하고 있는 것, 

clean_OOO : OOO에 대한 유효성 검사

middleware : view 에서  요청을 하면 그 때 실행되는 무언가

0505 study
Static 폴더 : 관리자가 필요해서 올린 파일
media 폴더 : 사용자가 올린 파일

AJAX : 비동기 데이터 보낼 때 // instagram / facebook
SPA : single page aplication // vue.js / react

JWT : JSON WEB Token요즘 토큰이라하면 JWT를 사용