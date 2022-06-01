from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class CustomUser(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    bio=models.TextField(null=True,blank=True)
    name=models.CharField(max_length=50)

class BlogPost(models.Model):
    title=models.CharField(max_length=50)
    content=models.TextField(null=True,blank=True)
    author=models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    files=models.FileField(upload_to='blog_files/',null=True,blank=True)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
class Comment(models.Model):
    com_content=models.TextField(null=True,blank=True)
    post=models.ForeignKey(BlogPost,related_name="comments",on_delete=models.CASCADE,null=True)
    com_author=models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    name=models.CharField(max_length=255,null=True)

class Block(models.Model):
    other_user=models.ForeignKey(User,on_delete=models.CASCADE,null=True,related_name='other_user')
    blocked_user=models.ForeignKey(User,on_delete=models.CASCADE,null=True,related_name='blocked_user')