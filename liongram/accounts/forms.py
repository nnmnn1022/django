from tabnanny import verbose
from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm

class UserBaseForm(forms.ModelForm) :
    class Meta :
        model = get_user_model()
        fields = '__all__'


# class UserCreateForm(UserBaseForm) :
#     password2 = forms.CharField(widget=forms.PasswordInput(), label='비밀번호 확인')
#     class Meta(UserBaseForm.Meta) :
#         fields = [ 'username', 'email', 'phone', 'password' ]


class UserSignupForm(UserCreationForm) :
    class Meta(UserCreationForm.Meta) :
        model = get_user_model()
        fields = ['username', 'email', 'profile_image']


