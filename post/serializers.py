from rest_framework import serializers

from .models import Post

class PostSimpleSerializer(serializers.ModelSerializer):
    # 전체 조회 시리얼라이저
    class Meta:
        model = Post
        fields = ('id', 'title')


class PostDetailSerializer(serializers.ModelSerializer):
    # 상세 조회 (게시글 내용) 시리얼라이저
    class Meta:
        model = Post
        fields = ('id' , 'title' , 'content' , 'created')


class PostCreateSerializer(serializers.ModelSerializer):
    # 게시물 생성 시리얼라이저
    class Meta:
        model = Post
        fields = ('title', 'content')

