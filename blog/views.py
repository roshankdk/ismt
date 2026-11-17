from django.shortcuts import get_object_or_404, render

from .models import Post


def blog_list(request):
    posts = Post.objects.filter(published=True).select_related('author', 'category')
    return render(request, 'blog/post_list.html', {'posts': posts})


def post_detail(request, slug):
    post = get_object_or_404(Post, slug=slug, published=True)
    return render(request, 'blog/post_detail.html', {'post': post})
