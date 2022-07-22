from ast import Delete
import imp
from turtle import pos
from urllib import response
from django.shortcuts import render

from rest_framework.generics import get_object_or_404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
# Create your views here.

from .models import Post
from .serializers import PostSimpleSerializer,PostDetailSerializer,PostCreateSerializer

from .models import Calendar
from .serializers import CalCreateSerializer, CalSimpleSerializer, CalDetailSerializer


# --------------공지게시판------------------

class PostsAPIView(APIView):
    # 공지글 전체 조회 뷰 (정렬)
    def get(self,request):
        # GET /post/
        posts = Post.objects.all()
        # 공지글 데이터 모두 가져오기
        serializer = PostSimpleSerializer(posts,many=True)
        # 직렬화
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self,request):
        # POST /post/
        serializer = PostCreateSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        # 유효성 검사 진행 후 값이 유효하면 저장하면, 유효하지 않으면 에러를 출력하도록 한다.


class PostAPIView(APIView):
    # 공지글 상세조회
    def get(self, request, pk):
        # GET /post/<pk>
        # 공지글 상세목록 보여주기
        post = get_object_or_404(Post, id=pk)
        # 데이터 없으면 404 오류
        serializer =  PostDetailSerializer(post)
        # 직렬화
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, pk):
        # PUT /post/<pk>
        # 글 수정
        post = get_object_or_404(Post, id=pk)
        serializer = PostCreateSerializer(post,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        # DELETE /post/<pk>
        # 글 삭제
        post = get_object_or_404(Post, id=pk)
        post.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


# -----------------------------------------


# --------------일정게시판------------------


class CalsAPIView(APIView):
    # 일정 전체 조회 뷰 (정렬)
    def get(self,request):
        # GET /cal/
        cals = Calendar.objects.all()
        # 일정 데이터 모두 가져오기
        serializer = CalSimpleSerializer(cals,many=True)
        # 직렬화
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self,request):
        # POST /cal/
        serializer = CalCreateSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        # 유효성 검사 진행 후 값이 유효하면 저장하면, 유효하지 않으면 에러를 출력하도록 한다.


class CalAPIView(APIView):
    # 일정 상세조회
    def get(self, request, pk):
        # GET /cal/<pk>
        # 일정 상세목록 보여주기
        cal = get_object_or_404(Calendar, id=pk)
        # 데이터 없으면 404 오류
        serializer =  CalDetailSerializer(cal)
        # 직렬화
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, pk):
        # PUT /cal/<pk>
        # 글 수정
        cal = get_object_or_404(Calendar, id=pk)
        serializer = CalCreateSerializer(cal,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        # DELETE /cal/<pk>
        # 글 삭제
        cal = get_object_or_404(Calendar, id=pk)
        cal.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
# -----------------------------------------