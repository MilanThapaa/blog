from django import template
from ..models import Post

register = template.Library()


@register.simple_tag
def total_posts():
    return Post.published_objects.count()


@register.inclusion_tag('blog/post/latest_posts.html')
def show_latest_posts(count=5):
    latest_posts = Post.published_objects.order_by('-publish')[:count]
    return {'latest_posts': latest_posts}
