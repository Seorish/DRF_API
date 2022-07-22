from django.shortcuts import render

from rest_framework.generics import get_object_or_404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
# Create your views here.

from .models import Post
from .serializers import PostSimpleSerializer,PostDetailSerializer,PostCreateSerializer

class PostsAPIView(APIView):
    # 게시글 조회 뷰 (정렬)
    def get(self,request):
        # GET /post/
        posts = Post.objects.all()
        # 게시글 데이터 모두 가져오기
        serializer = PostSimpleSerializer(posts,many=True)
        # 직렬화
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self,request):
        serializer = PostCreateSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        # 유효성 검사 진행 후 값이 유효하면 저장하면, 유효하지 않으면 에러를 출력하도록 한다.


class PostAPIView(APIView):
    # 게시글 상세조회
    def get(self, request, pk):
        # 게시글 상세목록 보여주기
        post = get_object_or_404(Post, id=pk)
        # 데이터 없으면 404 오류
        serializer =  PostDetailSerializer(post)
        # 직렬화
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, pk):
        post = get_object_or_404(Post, id=pk)
        serializer = PostCreateSerializer(post,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


