from django.db import models

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=100)
    # 게시글 제목
    content = models.TextField()
    # 게시글 본문
    created = models.DateTimeField(auto_now_add=True)
    # 게시글 생성 일자

    def __str__(self):
        return self.title
        # 인스턴스 출력 시 문자열로 설명
