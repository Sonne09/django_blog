from django.shortcuts import render


posts = [
    {
        'author': 'Sonne',
        'title': 'Blog Post 1',
        'content': 'First post content',
        'date_posted': 'Janaury 17, 2022'
    },
    {
        'author': 'Sandy',
        'title': 'Blog Post 2',
        'content': 'Second post content',
        'date_posted': 'Janaury 18, 2022'
    }
]


def home(request):
    context = {
        'posts': posts
    }
    return render(request, 'blog/home.html', context)

def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})