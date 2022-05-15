from django.contrib import admin
from django.db import router
from django.urls import path, include
from rest_framework import routers
from posts.views import PostModelViewSet, PostRetrieveUpdateDestoryView, calculator, PostListCreateView
from accounts.views import login_view

router = routers.DefaultRouter()
router.register('posts', PostModelViewSet)
# router.register('Comment', CommentModelViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
    # path('posts/', PostListCreateView.as_view(), name='post-list-create'),
    # path('posts/<int:pk>', PostRetrieveUpdateDestoryView.as_view(), name='post-detial-update'), # 이 <pk>는 꼭 지켜줘야 됨
    path('calculator/', calculator, name='calculator'),
    path('login/', login_view, name='login'),
    
]


