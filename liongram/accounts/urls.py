from django.urls import path

from accounts.views import login_view, logout_view, signup_view, update_view

app_name = 'accounts'

urlpatterns = [
    path('signup/', signup_view, name='signup'),
    path('login/', login_view, name='login'),
    path('update/', update_view, name='update'),
    path('logout/', logout_view, name='logout'),

]