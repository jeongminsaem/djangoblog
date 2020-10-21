from django.db import models
from django.urls import reverse

# Create your models here.
class GuestPost(models.Model):
    title = models.CharField(max_length=200)
    title_image = models.ImageField(blank=True)
    content = models.TextField()
    createDate = models.DateTimeField(auto_now_add=True)  
    writer = models.CharField(max_length=50 , default = '')
    readcnt = models.IntegerField(default=0)

    def __str__(self):
        return self.title
