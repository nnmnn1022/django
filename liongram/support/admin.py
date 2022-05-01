from tabnanny import verbose
from django.contrib import admin

from support.models import Faq, Inquiry, Answer

class AnswerInline(admin.TabularInline):
    model = Answer
    verbose_name = '답변'
    verbose_name_plural = '답변'
    extra = 0
    readonly_fields = ('created_at', 'created_by', 'last_modified_at', 'last_modified_by')
    fk_name = 'Inquiry'

# Register your models here.
@admin.register(Faq)
class FaqModelAdmin(admin.ModelAdmin): 
    list_display = ('category','question','last_modified_at')

    list_filter = ('category',)
    search_fields = ('question',)
    search_help_text = '질문 제목으로 검색이 가능합니다.'
    # 나중에 login 및 session을 배우고 나면 view단에서 생성자, 수정자를 지정해 줄 수 있을 것 같아 일단 생성자, 수정자를 readonly로 지정했음
    readonly_fields = ('created_at', 'created_by', 'last_modified_at', 'last_modified_by')

@admin.register(Inquiry)
class InquiryModelAdmin(admin.ModelAdmin): 
    list_display = ('category','title','created_by', 'created_at')

    list_filter = ('category',)
    search_fields = ('title', 'email', 'phone_number')
    search_help_text = '질문 제목, E-mail, 휴대전화 번호로 검색이 가능합니다.'
    # 나중에 login 및 session을 배우고 나면 view단에서 생성자, 수정자를 지정해 줄 수 있을 것 같아 일단 생성자를 readonly로 지정했음
    readonly_fields = ('created_at', 'created_by', 'last_modified_at', 'last_modified_by')
    inlines = [AnswerInline]