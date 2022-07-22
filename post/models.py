from django.db import models

# Create your models here.

class Post(models.Model):
    # 공지글 클래스
    title = models.CharField(max_length=100)
    # 공지글 제목
    content = models.TextField()
    # 공지글 본문
    created = models.DateTimeField(auto_now_add=True)
    # 공지글 생성 일자

    def __str__(self):
        return self.title
        # 인스턴스 출력 시 문자열로 설명


class Calendar(models.Model):
    # 일정관리 클래스
    calendar_title = models.CharField(max_length=100)
    # 일정 제목 및 내용
    calendar_final = models.DateField()
    # 일정 기한(직접 설정 가능하도록)
    calendar_created = models.DateTimeField(auto_now_add=True)
    # 게시글 생성 일자
    calendar_damdang = models.CharField(max_length=10)

    def __str__(self):
        return self.calendar_title
        # 인스턴스 출력 시 문자열로 설명