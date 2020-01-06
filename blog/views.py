from django.shortcuts import render

posts = [
    {
        'author': 'RyanN',
        'title': 'Blog Post 1',
        'content': 'First Post',
        'date_posted': 'Dec 12, 2019'
    },
    {
        'author': 'John Doe',
        'title': 'Blog Post 2',
        'content': 'Second Post',
        'date_posted': 'Dec 25, 2019'
    }
]

# Create your views here.
def home(request):
    context = {
        'posts': posts
    }
    return render(request, 'blog/home.html', context)

def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})