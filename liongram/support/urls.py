from xml.etree.ElementInclude import include
from django.contrib import admin
from django.urls import path

from support.views import faq_create_view, faq_delete_view, faq_detail_view, faq_list_view, faq_update_view 

app_name = 'support'

urlpatterns = [
    path('', faq_list_view, name='faq_list'),
    path('new/', faq_create_view, name='faq_create'),
    # Django에서 지원하는 변수(정규 표현식 대용인듯)
    path('<int:id>', faq_detail_view, name='faq_detail'),
    path('<int:id>/edit/', faq_update_view, name='faq_modify'),
    path('<int:id>/delete/', faq_delete_view, name='faq_delete'),

]