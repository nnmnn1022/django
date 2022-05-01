from django.db import models
from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _
from config.models import BaseModel

# Create your models here.
User = get_user_model()

class Faq(BaseModel):

    class Category(models.TextChoices):
        GENERAL = 'GEN', _('General issue')
        ACCOUNT = 'ACC', _('Account issue')
        ETC = 'ETC', _('etc.')
        # PAYMENT = 'PAY', _('Payment')
        # POST = 'POST', _('Post')
        # DIRECTMESSAGE = 'DM', _('DirectMessage')
        # REELS = 'REEL', _('Reels')
        # CAMERAFILTER = 'FILT', _('CameraFilter')

    question = models.CharField(verbose_name='질문', max_length=64)
    category = models.CharField(max_length=3,
        choices=Category.choices,
        default=Category.GENERAL)
    faq_answer = models.TextField(verbose_name='답변',blank=True)
    created_by = models.ForeignKey(to=User, verbose_name='작성자', on_delete=models.CASCADE, related_name='faq_creater', blank=True, null=True)
    last_modified_by = models.ForeignKey(to=User, verbose_name='수정자', on_delete=models.CASCADE, related_name='faq_last_modifier', blank=True, null=True)


class Inquiry(BaseModel):
    class Category(models.TextChoices):
        GENERAL = 'GEN', _('General issue')
        ACCOUNT = 'ACC', _('Account issue')
        ETC = 'ETC', _('etc.')

    class Status(models.TextChoices):
        REGISTED = 'REG', _('문의 등록')
        CHECKING = 'CHE', _('접수 완료')
        COMPLETE = 'COM', _('답변 완료')
        NOTIFIED = 'NOT', _('알림 완료')

    category = models.CharField(max_length=3,
        choices=Category.choices,
        default=Category.GENERAL)
    


    title = models.CharField(verbose_name='질문 제목', max_length=64)
    status = models.CharField(max_length=3,
        choices=Status.choices,
        default=Status.REGISTED
    )
    email = models.EmailField(verbose_name='e-mail')
    email_checkbox = models.BooleanField(verbose_name='e-mail로 답변을 받겠습니다.')

    phone_number = models.CharField(verbose_name='전화번호', max_length=11)
    phone_checkbox = models.BooleanField(verbose_name='문자메시지로 답변을 받겠습니다.')
    detail = models.TextField(verbose_name='내용')

    image = models.ImageField(verbose_name='이미지', blank=True, null=True)
    dateTimeOfUpload = models.DateTimeField(auto_now = True)
    created_by = models.ForeignKey(to=User, verbose_name='작성자', on_delete=models.CASCADE, related_name='inquiry_creater', blank=True, null=True)
    last_modified_by = models.ForeignKey(to=User, verbose_name='수정자', on_delete=models.CASCADE, related_name='inquiry_last_modifier', blank=True, null=True)

class Answer(BaseModel):
    content = models.TextField(verbose_name='내용')
    # 외래키와 연동 및 종속되도록 설정
    Inquiry = models.ForeignKey(to='Inquiry', on_delete=models.CASCADE)
    # 사용자와 연결하기
    created_by = models.ForeignKey(to=User, verbose_name='작성자', on_delete=models.CASCADE, related_name='answer_creater', blank=True, null=True)
    last_modified_by = models.ForeignKey(to=User, verbose_name='수정자', on_delete=models.CASCADE, related_name='answer_last_modifier', blank=True, null=True)