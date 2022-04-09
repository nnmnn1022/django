from tabnanny import verbose
from django.contrib import admin
from .models import Post, Comment

# 본인이 만든 모델을 admin에서 볼 수 있도록 추가

class CommentInline(admin.TabularInline):
    model = Comment
    verbose_name = '댓글'
    verbose_name_plural = '댓글'
    #추가
    extra = 1
    #최소
    min_num = 0
    # max_num = 5


# admin.site.register(app) 가 아닌 @admin.register(app)으로 대체
@admin.register(Post)
class PostModelAdmin(admin.ModelAdmin): 

    list_display = ('id','image','content','created_at','view_count','writer')
    #list_editable = ('content',)
    # 튜플로 넣는 이유는 model admin에 들어가보면 튜플로 정의가 되어 있기 때문에 튜플로.
    # 튜플의 경우 한 개 요소 밖에 없을 때 쉼표를 꼭 넣어줘야 한다.
    list_filter = ('created_at', )
    search_fields = ('id', 'writer__username')
    search_help_text = '게시판 번호, 작성자 검색이 가능합니다.'
    # 자동으로 추가되어 보이지 않던 created_at 필드의 경우
    # readonly_feilds를 사용해서 넣어주면 볼 수 있음
    readonly_fields = ('created_at', 'view_count')

    inlines = [CommentInline]
    actions = ['make_published']

    def make_published(modeladmin, request, queryset):
        for item in queryset :
            item.content = '운영 규칙 위반으로 인한 삭제 처리'
            item.save()
