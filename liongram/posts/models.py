from django.db import models
from django.contrib.auth import get_user_model
from config.models import BaseModel

# Create your models here.
User = get_user_model()

class Post(BaseModel) :
    image = models.ImageField(verbose_name='이미지', null=True, blank=True)
    content = models.TextField(verbose_name='내용')
    view_count = models.IntegerField(verbose_name='조회수', default=0)
    writer = models.ForeignKey(verbose_name='작성자', to=User, on_delete=models.CASCADE, null=True, blank=True)

class Comment(BaseModel) :
    content = models.TextField(verbose_name='내용')
    # 외래키와 연동 및 종속되도록 설정
    post = models.ForeignKey(to='Post', on_delete=models.CASCADE)
    # 사용자와 연결하기
    writer = models.ForeignKey(to=User, on_delete=models.CASCADE)