from django import forms
from posts.models import Post



# class PostBaseForm(forms.Form):
#     CATEGORY_CHOICES =[
#         ('1', '일반'),
#         ('2', '계정'),
#     ]

#     image = forms.ImageField(label='이미지', required=True)
#     # text field는 따로 없음
#     content = forms.CharField(label='내용', widget=forms.Textarea, required=True)
#     # category = forms.ChoiceField(label='카테고리', choices=CATEGORY_CHOICES)

# ModelForm을 상속 받을 때는 Meta 클래스라는 걸 작성해줘야 함
class PostBaseForm(forms.ModelForm):
    
    class Meta :
        model = Post
        fields = '__all__'

from django.core.exceptions import ValidationError
class PostCreateForm(PostBaseForm):
    class Meta(PostBaseForm.Meta):
        fields = ['image', 'content']

    # clean_ + 필드 이름을 통해서 그 필드의 유효성을 검사하도록 한다는 것은 약속이래요..
    def clean_content(self) :
        data = self.cleaned_data['content']
        if '비속어' == data :
            raise ValidationError('\'비속어\'는 사용하실 수 없습니다.')
        
        return data

class PostUpdateForm(PostBaseForm):
    class Meta(PostBaseForm.Meta):
        fields = ['image', 'content']

class PostDetailForm(PostBaseForm):
    def __init__(self, *args, **kwargs):
        super(PostDetailForm, self).__init__(*args, **kwargs)
        # for field in self.fields :
            # field.widget.attrs['disabled'] = True
        for key in self.fields:
            self.fields[key].widget.attrs['disabled'] = True