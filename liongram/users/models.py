from tkinter import CASCADE
from django.db import models
from django.contrib.auth.models import AbstractUser, UserManager as DjangoUserManager

# Manager는 DB로 쿼리를 날릴 때 Django 가 제공하는 인터페이스
class UserManager(DjangoUserManager) :
    def _create_user(self, username, email, password, **extra_fields):
        if not email :
            raise ValueError('이메일은 필수 값입니다.')
        user = self.model(username=username, email=email, **extra_fields)
        # 해싱을 해서 넣는 이유 (암호화, 복호화) : 비밀번호를 관리자도 알 수 없게 하기 위해.
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, username, email=None, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(username, email, password, **extra_fields)
    
    def create_superuser(self, username, email=None, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self._create_user(username, email, password, **extra_fields)


class User(AbstractUser) :
    phone = models.CharField(verbose_name='전화번호', max_length=11)
    # 우리가 커스터마이징한 usermanager 모델을 연결
    objects = UserManager()




# 들어가긴 하지만 많이 쓰이지 않는다고 했을 때, 아래와 같이 확장하여 사용할 수도 있음.
# class UserInfo(models.Model):
#     phone_sub = models.CharField(verbose_name='보조 전화번호', max_length=11)
#     user = models.ForeignKey(to='User', on_delete=CASCADE)