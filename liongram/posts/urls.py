from xml.etree.ElementInclude import include
from django.contrib import admin
from django.urls import path

from posts.views import class_view, function_list_view, function_view, post_create_form_view, post_create_view, post_delete_view, post_detail_view, post_list_view, post_update_view, url_prameter_view, url_view, comment_create

app_name = 'posts'

urlpatterns = [
    path('', post_list_view, name='post_list'),
    path('create/', post_create_form_view, name='post-create'),
    # Django에서 지원하는 변수(정규 표현식 대용인듯)
    path('<int:id>', post_detail_view, name='post-detail'),
    path('<int:id>/edit/', post_update_view, name='post-edit'),
    path('<int:id>/delete/', post_delete_view, name='post-delete'),
    path('comment/<int:id>/create/', comment_create, name='comment-create'),

]