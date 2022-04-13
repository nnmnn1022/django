"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from posts.views import url_prameter_view, url_view

# Django에서 지원하는 변수(정규 표현식 대용인듯)
urlpatterns = [
    path('admin/', admin.site.urls),
    path('url/', url_view),
    # 경로로 받기
    path('url/<str:username>/', url_prameter_view)
]
