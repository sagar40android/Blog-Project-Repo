from django import template
from blog.models import Post
from django.db.models import Count
register=template.Library()

@register.simple_tag(name="my_tag")
def total_posts():
    return Post.objects.count()

@register.inclusion_tag('blog/latest_post.html')
def show_latest_post(count=3):
    latest_post=Post.objects.order_by('-publish')[:count]
    return {'latest_post':latest_post}
  

# @register.assignment_tag
@register.simple_tag
def get_most_commented_tag(count=5):
    return Post.objects.annotate(total_comment=Count('comments')).order_by('-total_comment')[:count]
