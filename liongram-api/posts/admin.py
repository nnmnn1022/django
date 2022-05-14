from django.contrib import admin

from posts.models import Post, Comment
from django.contrib import admin

class CommentInline(admin.TabularInline) :
    model = Comment
    verbose_name = '댓글'
    verbose_name_plural = '댓글'
    #추가
    extra = 1
    #최소
    min_num = 0

# Register your models here.
@admin.register(Post)
class PostModelAdmin(admin.ModelAdmin) :
    inlines = [CommentInline]