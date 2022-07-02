from django.shortcuts import render, get_object_or_404
from .models import Post


def post_list(request):
    post = Post.published_objects.all()

    context = {
        'post': post
    }

    return render(request, 'blog/list.html', context)
