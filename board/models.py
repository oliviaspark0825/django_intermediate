from django.db import models

# Create your models here.
class Board(models.Model):
    title = models.CharField(max_length=10)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    
    def __str__(self):
        return f"{self.id}:{self.title}"
        return self.title

class Comment(models.Model):
    # 참조하는 부모객체를 소문자로 주로 씀, 첫번째 객체는 부모객체
    board = models.ForeignKey(Board, on_delete=models.CASCADE) # foreignkey 필수인자, 게시물이 지워졌을 때, 그 아래 달린 댓글들을 어떻게 할 것인가
    #참조하는 부모객체가 사라졌을 때, 부모에 딸려있는 자식 객체들을 어떻게 처리할지 정의한다
    content = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    
    def __str__(self):
        return self.content

