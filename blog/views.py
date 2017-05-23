# -*- coding: utf-8 -*-
# import pdb; pdb.set_trace()
from __future__ import unicode_literals
from django.utils import timezone

from .models import Post
from django.contrib.auth.models import User

from .forms import PostForm

from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse

# Create your views here.

def post_list(request):
    # posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    # 公開非公開関係なく表示
    posts = Post.objects.filter(created_date__lte=timezone.now()).order_by('created_date').reverse
    # import pdb; pdb.set_trace()
    # さらに表示順を逆にする(追加された順の逆)
    return render(request, 'blog/post_list.html', {'posts': posts})

def post_detail(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    # post = Post.objects.get(pk=post_id)
    return render(request, 'blog/post_detail.html', {'post': post})
    
def post_edit(request, post_id=None):
    # import pdb; pdb.set_trace()
    post = get_object_or_404(Post, pk=post_id)
    if request.method == 'POST':
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            if request.user.is_authenticated():
                post.author = request.user
                post.save()
            else:
                return redirect('post_list')
            return redirect('post_detail', post_id=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/post_edit.html', {'form': form})
    # return render(request, 'blog/post_edit.html', {'form': form}, dict(form=form, post_id=post_id))

def post_delete(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    if request.user.is_authenticated():
        post.delete()
    else:
        return redirect('post_list')
    return redirect('post_list')

def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            if request.user.is_authenticated():
                post.save()
            else:
                return redirect('post_list')
            return redirect('post_detail', post_id=post.pk)
    else:
        form = PostForm()
    return render(request, 'blog/post_new.html', {'form': form})
