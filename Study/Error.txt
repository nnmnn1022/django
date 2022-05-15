ERRORS:
support.Faq.modifier: (fields.E304) Reverse accessor for 'support.Faq.modifier' clashes with reverse accessor for 'support.Faq.writer'.
        HINT: Add or change a related_name argument to the definition for 'support.Faq.modifier' or 'support.Faq.writer'.
support.Faq.writer: (fields.E304) Reverse accessor for 'support.Faq.writer' clashes with reverse accessor for 'support.Faq.modifier'.
        HINT: Add or change a related_name argument to the definition for 'support.Faq.writer' or 'support.Faq.modifier'.
		
>> 해결 방법 : foreign key가 두 개일 때 특히나 참고하는 내용이 비슷할 때
아마도 참고할만한 related_name 지정이 필요한 것 같음

"detail": "메소드(Method) \"GET\"는 허용되지 않습니다.

 type object 'Token' has no attribute 'objects' :
 settings/ Installed APPS에 아래 내용 추가
rest_framework.authtoken

Access to XMLHttpRequest at 'http://localhost:8000/posts/' from origin 'null' has been blocked by CORS policy: No 'Access-Control-Allow-Origin' header is present on the requested resource.
: pip install django-cors-headers
이후
settings.py/INSTALLED APPS에 `corsheaders` 추가
MIDDLEWARE에도 `corsheaders.middleware.CorsMiddleware` 추가
> 이 부분을 추가할 때는  최대한 많은 응답에 헤더를 추가할 수 있도록 `django.middleware.common.CommonMiddleware`나 Whitenoise의 WhiteNoiseMiddleware 보다 위에 위치 시켜야 함

`CORS_ORIGIN_ALLOW_ALL = FALSE
CORS_ORIGIN_WHITELIST = (
    'http://localhost:8000'
	'http://127.0.0.1:8000'
)` 추가 프론트 쪽에서 쓰고자 하는 포트 번호도 넣어주면 되는 듯