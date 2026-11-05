from django.shortcuts import render

def blog_list(request):
    posts = [
        {'title': 'First Blog Post', 'content': 'This is my first blog post.'},
        {'title': 'Second Blog Post', 'content': 'This is my second blog post.'},
        {'title': 'Third Blog Post', 'content': 'This is my third blog post.'},
    ]
    return render(request, 'blog_list.html', {'posts': posts})
