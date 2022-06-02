from django.db import models
from django.contrib.auth.models import User
# Create your models here.
from django.db.models.signals import post_save


class CustomUser(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE,null=True)
    bio=models.TextField(null=True,blank=True)
    name=models.CharField(max_length=50)
    proffesion=models.CharField(max_length=50,null=True)
    skills=models.TextField(null=True,blank=True)

    def __str__(self):
        return self.user.username

    def create_profile(sender,**kwargs):
        if kwargs['created']:
            user_profile=CustomUser.objects.create(user=kwargs['instance'])

    post_save.connect(create_profile,sender=User)
class Block(models.Model):
    other_user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, null=True, related_name='other_user')
    blocked_user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, null=True, related_name='blocked_userr')

class BlogPost(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField(null=True, blank=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    files = models.FileField(upload_to='blog_files/', null=True, blank=True)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    blocked_userr = models.ForeignKey(CustomUser, on_delete=models.CASCADE, null=True)


class Comment(models.Model):
    com_content = models.TextField(null=True, blank=True)
    post = models.ForeignKey(BlogPost, related_name="comments", on_delete=models.CASCADE, null=True)
    com_author = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=255, null=True)

