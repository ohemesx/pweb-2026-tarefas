from django.shortcuts import render
from .models import Post
from django.shortcuts import get_object_or_404

def index(request):
    posts = Post.objects.all()
    context = {
        'posts': posts,
    }
    return render(request, 'blog/index.html', context)

def post(request, id):
    post = get_object_or_404(Post, id=id)
    context = {
        'post': post,
    }
    return render(request, 'blog/post.html', context)