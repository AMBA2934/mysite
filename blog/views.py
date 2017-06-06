# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth.models import User
from django.core.exceptions import PermissionDenied
from django.shortcuts import render, redirect
from blog.models import Post, Comment


def home(request):
    template_name = 'blog/home.html'
    posts = Post.objects.all()
    for i in posts:
        i.content = i.content[0:100] + "....."
    context = {'object_list': posts}
    return render(request, template_name, context)


def post_detail(request, pk):
    template_name = 'blog/post.html'
    post = Post.objects.get(id=int(pk))
    comments = Comment.objects.filter(post=post)
    context = {'post': post, 'comments': comments}

    if request.method == "POST":
        comment_text = request.POST['comment_text']
        co =Comment(comment_text=comment_text, post=post, )
        co.save()
        return redirect('post',post.id)

    return render(request, template_name, context)

def edit_post(request, pk):
    post = Post.objects.get(id=int(pk))
    if request.method == "GET":
        template_name = 'blog/post_edit.html'
        context = {'post': post}
        return render(request, template_name, context)
    else:
        post.title = request.POST['title']
        post.content = request.POST['content']
        post.is_published = request.POST['is_published']
        post.img = request.FILES['img']
        post.save()
        return redirect('post', post.id)

def add_post(request):
    if request.method == "POST":
        title= request.POST['title']
        content= request.POST['content']
        img=request.FILES['img']
        is_published=request.POST['is_published']
        user=User.objects.get(username=request.user.username)
        new_post=Post(title=title,content=content,img=img,is_published=is_published, user=user)
        new_post.save()
        return redirect('post',new_post.id)
    else:
        template_name='blog/add_post.html'
        context={}
        return render(request,template_name,context)

def edit_post(request, pk,):
    post=Post.objects.get(id=int(pk))
    if request.user.username!=post.user.username:
        raise PermissionDenied
    if request.method == "GET":
        template_name = 'blog/post_edit.html'
        context={'post':post}
        return render(request,template_name,context)
    else:
        post.title = request.POST['title']
        post.content= request.POST['content']

        if 'img' in request.FILES:
            post.img = request.FILES['img']
        if 'is_published' in request.POST:
            post.is_published = request.POST['is_published']

        post.save()
        return redirect('post',post.id)


def del_post(request, id):
    if Post.objects.get(id=id) is not None:
        post=Post.objects.get(id=id)
        if post.user.username == request.user.username:
            post.delete()
            return redirect('home')
    raise PermissionDenied


