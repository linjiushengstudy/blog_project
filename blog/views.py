# blog/views.py

from django.shortcuts import render, get_object_or_404
from .models import Post, Comment


def post_list(request):
    posts = Post.objects.all()
    return render(request, 'blog/post_list.html', {'posts': posts})


def add_comment(request, post_id):
    post = Post.objects.get(pk=post_id)
    if request.method == 'POST':
        text = request.POST['comment_text']
        Comment.objects.create(post=post, text=text)
    return render(request, 'blog/post_detail.html', {'post': post})


def post_detail(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    return render(request, 'blog/post_detail.html', {'post': post})
