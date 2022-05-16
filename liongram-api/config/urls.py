from django.contrib import admin
from django.db import router
from django.urls import path, include, re_path
from rest_framework import routers
from posts.views import PostModelViewSet, PostRetrieveUpdateDestoryView, calculator, PostListCreateView
from accounts.views import login_view, LoginView
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from django.views.generic import TemplateView

schema_view = get_schema_view(
    openapi.Info(
        title="Snippets API",
        default_version='v1',
        scription="Test description",
        rms_of_service="https://www.google.com/policies/terms/",
        ntact=openapi.Contact(email="contact@snippets.local"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=[permissions.AllowAny],
)

router = routers.DefaultRouter()
router.register('posts', PostModelViewSet)
# router.register('Comment', CommentModelViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
    # path('posts/', PostListCreateView.as_view(), name='post-list-create'),
    # path('posts/<int:pk>', PostRetrieveUpdateDestoryView.as_view(), name='post-detial-update'), # 이 <pk>는 꼭 지켜줘야 됨
    path('calculator/', calculator, name='calculator'),
    # path('login/', login_view, name='login'),
    path('login/', LoginView.as_view(), name='login'),
    re_path(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    re_path(r'^swagger/$', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    re_path(r'^redoc/$', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    
]


