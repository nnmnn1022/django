from dataclasses import fields
from rest_framework.serializers import ModelSerializer, HyperlinkedModelSerializer
from .models import Post, Comment

# 베이스 모델
class PostBaseModelSerializer(ModelSerializer) :
    class Meta :
        model = Post
        fields = '__all__'

# 게시글 목록
class PostListModelSerializer(PostBaseModelSerializer) :
    class Meta(PostBaseModelSerializer.Meta) :
        fields = [
            'id',
            'image',
            'content',
            'created_at',
            'view_count',
            'writer',
        ]
        depth = 0

# 게시글 상세
class PostRetrieveModelSerializer(PostBaseModelSerializer) :
    class Meta(PostBaseModelSerializer.Meta) :
        fields = [
            'id',
            'image',
            'content',
            'created_at',
            'view_count',
            'writer',
        ]
        depth = 2

# 게시글 생성
class PostCreateModelSerializer(PostBaseModelSerializer) :
    class Meta(PostBaseModelSerializer.Meta) :
        fields = [
            'image',
            'content',
        ]

# 게시글 삭제
class PostDeleteModelSerializer(PostBaseModelSerializer) :
    pass

class CommentHyperlinkModelSerializer(HyperlinkedModelSerializer) :
    class Meta :
        model = Post
        fields = '__all__'


class CommentListModelSerializer(ModelSerializer) :
    class Meta :
        model = Comment
        fields = '__all__'