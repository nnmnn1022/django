from django.contrib import admin

from support.models import Faq

# Register your models here.
@admin.register(Faq)
class FaqModelAdmin(admin.ModelAdmin): 
    list_display = ('category','question','answer', 'created_by', 'created_at')

    list_filter = ('created_at', 'created_by', 'category')
    search_fields = ('id', 'writer__username')
    search_help_text = '게시판 번호, 작성자 검색이 가능합니다.'
    # 나중에 login 및 session을 배우고 나면 view단에서 생성자, 수정자를 지정해 줄 수 있을 것 같아 일단 생성자, 수정자를 readonly로 지정했음
    readonly_fields = ('created_at', 'created_by','modified_at', 'last_modifier')