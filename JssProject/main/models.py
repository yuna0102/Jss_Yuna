from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Jasoseol(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField()
    updated_at = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    #on_delete 속성은 만약 연결된 오브젝트가 지워지면 어떻게 할 것인가?에 대한 것을 미리 정의
    #예를 들어 회원탈퇴>오브젝트 삭제