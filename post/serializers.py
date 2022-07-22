from rest_framework import serializers

from .models import Post,Calendar

class PostSimpleSerializer(serializers.ModelSerializer):
    # 공지글 전체 조회 시리얼라이저
    class Meta:
        model = Post
        fields = ('id', 'title')


class PostDetailSerializer(serializers.ModelSerializer):
    # 공지글 상세 조회 시리얼라이저
    class Meta:
        model = Post
        fields = ('id' ,'title' , 'content' , 'created')


class PostCreateSerializer(serializers.ModelSerializer):
    # 공지글 생성 시리얼라이저
    class Meta:
        model = Post
        fields = ('title', 'content','created')


class CalSimpleSerializer(serializers.ModelSerializer):
    # 일정 전체 조회 시리얼라이저
    class Meta:
        model = Calendar
        fields = ('id', 'calendar_title','calendar_final' ,'calendar_damdang')


class CalDetailSerializer(serializers.ModelSerializer):
    # 일정 상세 조회 시리얼라이저
    class Meta:
        model = Calendar
        fields = ('id' ,'calendar_title','calendar_final', 'calendar_damdang','calendar_created')


class CalCreateSerializer(serializers.ModelSerializer):
    # 일정 생성 시리얼라이저
    class Meta:
        model = Calendar
        fields = ('calendar_title','calendar_final', 'calendar_damdang', 'calendar_created')

        



