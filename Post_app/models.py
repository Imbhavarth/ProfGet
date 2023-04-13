from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='post')

    project_name = models.CharField(max_length=22,null=True)
    
    project_description = models.CharField(max_length=150, null=True)

    project_requirement = models.CharField(max_length=50, null=True)

    project_rate = models.CharField(max_length=20, null=True)

    upload_date = models.DateTimeField(auto_now_add=True, blank=True)

    class Meta:
        ordering = ['-upload_date',]

class Chat(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='chat')

    msg = models.CharField(max_length=150, null=True)

    upload_date = models.DateTimeField(auto_now_add=True, blank=True)

    class Meta:
        ordering = ['upload_date',]
