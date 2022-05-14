from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import api_view, action
from rest_framework.response import Response
from posts.serailizers import (PostBaseModelSerializer, PostListModelSerializer, PostCreateModelSerializer, CommentHyperlinkModelSerializer, PostRetrieveModelSerializer, CommentListModelSerializer)
from .models import Post, Comment
from rest_framework import generics, status

class PostModelViewSet(ModelViewSet) :
    queryset = Post.objects.all()
    serializer_class = PostListModelSerializer

    @action(detail=True, methods=['get'])
    def get_comment_all(self, request, pk=None) :
        post = self.get_object()
        comment_all = post.comment_set.all()
        serializer = CommentListModelSerializer(comment_all, many=True)
        return Response(serializer.data)

# class CommentModelViewSet(ModelViewSet) :
#     queryset = Comment.objects.all()
#     serializer_class = CommentHyperlinkModelSerializer

# 게시글 목록 + 작성
class PostListCreateView(generics.ListAPIView, generics.CreateAPIView) :
    queryset = Post.objects.all()
    serializer_class = PostListModelSerializer

    # 생성자 만들기 (오버라이딩)
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        # self.perform_create(serializer)
        # 로그인 안 된 상태에서 작업 될 경우의 예외 처리
        if request.user.is_authenticated :
            serializer.save(writer=request.user)
        else :
            serializer.save()
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

# 게시글 상세 + 수정 + 삭제
# Put은 전체 수정 / Patch는 입력 받은 값만 수정
class PostRetrieveUpdateDestoryView(generics.RetrieveAPIView, generics.UpdateAPIView, generics.DestroyAPIView) :
    queryset = Post.objects.all()
    serializer_class = PostRetrieveModelSerializer

# 게시글 삭제

@api_view()
def calculator(request) :
    # 1. 데이터 확인
    num1 = request.GET.get('num1', 0)
    num2 = request.GET.get('num2', 0)
    operators = request.GET.get('operators')

    # 2. 계산
    if operators == '+' :
        result = int(num1) + int(num2)
    elif operators == '-' :
        result = int(num1) - int(num2)
    elif operators == '*' :
        result = int(num1) * int(num2)
    elif operators == '/' :
        result = int(num1) / int(num2)

    # 3. 응답
    data = {
        'type' : 'FBV',
        'result' : result,
    }

    return Response(data)