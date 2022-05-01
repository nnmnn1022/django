from django.db import models
from django.contrib.auth import get_user_model
from django.utils import timezone

User = get_user_model()

class BaseModel(models.Model) :
    created_at = models.DateTimeField(verbose_name='작성일시',auto_now_add=True)
    last_modified_at = models.DateTimeField(verbose_name='수정일시',auto_now=True)

    class Meta :
        abstract = True