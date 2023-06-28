from django.shortcuts import render
from django.http import HttpResponse
from .models import Post
# Create your views here. Main page to edit the home page


def home(request):
    # The post context
    context = {
        # todo: add title
        'title': 'Home',
        'posts': Post.objects.all()
    }

    return render(request, 'blog/home.html', context)

def about(request):
    return render(request, 'blog/about.html')