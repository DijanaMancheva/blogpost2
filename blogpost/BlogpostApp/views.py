from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render

from .forms import BlogPostForm
from .models import BlogPost,CustomUser
from django.views.generic import DetailView
# Create your views here.
def posts(request):
    querySet=BlogPost.objects.all()
    context={"posts":querySet}
    return render(request,"posts.html",context=context)

def addpost(request):
    if request.method=="POST":
        form=BlogPostForm(request.POST)
        post=form.save(commit=False)

        post.user=request.user
        post.save()

    querySet=BlogPost.objects.all()
    context={"posts":querySet,"form":BlogPostForm}
    return render(request,"addpost.html",context=context)
@login_required()
def profile(request):

    querySet=CustomUser.objects.all()
    querySet1=BlogPost.objects.all()
    context={'custom_user':querySet,'posts':querySet1}

    return render(request,"profile.html",context=context)