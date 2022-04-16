from unicodedata import category
from django.db import models
from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _

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

    question = models.CharField(verbose_name='질문', max_length=30)
    category = models.CharField(max_length=4,
        choices=Category.choices,
        default=Category.GENERAL)
    answer = models.TextField(verbose_name='답변')
    created_by = models.ForeignKey(to=User, verbose_name='생성자', on_delete=models.CASCADE, related_name='creater', null=True, blank=True)
    created_at = models.DateTimeField(verbose_name='생성일시', auto_now_add=True)
    last_modifier = models.ForeignKey(to=User, verbose_name='최종 수정자', on_delete=models.CASCADE, related_name='modifier', null=True, blank=True)
    modified_at = models.DateTimeField(verbose_name='최종 수정일시', auto_now_add=True)

