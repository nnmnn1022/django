from unicodedata import category
from django.db import models
from django.contrib.auth import get_user_model
from django.forms import EmailField
from django.utils.translation import gettext_lazy as _
from django.utils import timezone

# Create your models here.
User = get_user_model()

class Faq(models.Model):

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
    answer = models.TextField(verbose_name='답변')
    created_by = models.ForeignKey(to=User, verbose_name='생성자', on_delete=models.CASCADE, related_name='creater', null=True, blank=True)
    # 첫번째 추가 할 땐 auto_now_add
    created_at = models.DateTimeField(verbose_name='생성일시', auto_now_add=True)
    last_modifier = models.ForeignKey(to=User, verbose_name='최종 수정자', on_delete=models.CASCADE, related_name='modifier', null=True, blank=True)
    # auto_now : 수정된 날짜 시에 사용
    modified_at = models.DateTimeField(verbose_name='최종 수정일시', auto_now='true')

class Inquiry(models.Model):
    class Category(models.TextChoices):
        GENERAL = 'GEN', _('General issue')
        ACCOUNT = 'ACC', _('Account issue')
        ETC = 'ETC', _('etc.')
    category = models.CharField(max_length=3,
        choices=Category.choices,
        default=Category.GENERAL)

    title = models.CharField(verbose_name='질문 제목', max_length=64)
    email = models.EmailField(verbose_name='e-mail')
    email_checkbox = models.BooleanField(verbose_name='e-mail로 답변을 받겠습니다.')

    phone_number = models.CharField(verbose_name='전화번호', max_length=11)
    phone_checkbox = models.BooleanField(verbose_name='문자메시지로 답변을 받겠습니다.')
    detail = models.TextField(verbose_name='내용')

    image = models.ImageField(verbose_name='이미지', upload_to='uploades/', blank=True, null=True)
    dateTimeOfUpload = models.DateTimeField(auto_now = True)
    
    created_at = models.DateTimeField(verbose_name='생성일시', auto_now_add=True)
    # session에서 유저 데이터를 받아와야 하지만, 아직 배우지 못한 부분이라 blank, null을 True로 처리해서 생성자 데이터가 없어도 데이터 입력 가능하도록 함
    created_by = models.ForeignKey(to=User, verbose_name='생성자', on_delete=models.CASCADE, related_name='inquiry_creater', blank=True, null=True)

class Answer(models.Model):
    content = models.TextField(verbose_name='내용')
    created_at = models.DateTimeField(verbose_name='생성일시', auto_now_add=True)
    # 외래키와 연동 및 종속되도록 설정
    Inquiry = models.ForeignKey(to='Inquiry', on_delete=models.CASCADE)
    # 사용자와 연결하기
    # session에서 유저 데이터를 받아와야 하지만, 아직 배우지 못한 부분이라 blank, null을 True로 처리해서 생성자 데이터가 없어도 데이터 입력 가능하도록 함
    writer = models.ForeignKey(to=User, related_name='Answer_writer', on_delete=models.CASCADE, blank=True, null=True)

    last_modifier = models.ForeignKey(to=User, verbose_name='최종 수정자', on_delete=models.CASCADE, related_name='Answer_modifier', blank=True, null=True)
    # auto_now : 수정된 날짜 시에 사용
    modified_at = models.DateTimeField(verbose_name='최종 수정일시', auto_now='true')