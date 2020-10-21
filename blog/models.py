from django.db import models
from django.urls import reverse

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=50, help_text="블로그 글의 분류를 입력하세요.(ex:일상)")

    def __str__(self):
        return self.name

#블로그 글(제목, 작성일, 내용, 작성자, 이름)
class Post(models.Model):
    title = models.CharField(max_length=200)
    title_image = models.ImageField(blank=True)
    content = models.TextField()
    createDate = models.DateTimeField(auto_now_add=True)  
    writer = models.CharField(max_length=50 , default = '')
    readcnt = models.IntegerField(default=0)

    def __str__(self):
        return self.title

    #1번 글의 경우 -> post/1
    def get_absolute_url(self):
        return reverse("post", args=[str(self.id)])

    def is_content_more50(self):
        return len(self.content) > 50
    
    def get_content_under50(self):
        return self.content[:50]
