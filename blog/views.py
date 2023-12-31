from typing import Optional
from django.forms.models import BaseModelForm
from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.http import HttpResponse
from .models import Post
from django.views.generic import (
    ListView, 
    CreateView, 
    DetailView,
    UpdateView,
    DeleteView
)

# def home(request):
#     """The view of each blog/post showing on the home page

#     Args:
#         request (html request): _description_

#     Returns:
#        None
#     """

#     # The post context. Each post contain a title and post. The post object is defined 
#     # under models.py
#     context = {
#         # todo: add title
#         'title': 'Home',
#         'posts': Post.objects.all()
#     }

#     return render(request, 'blog/home.html', context)


class PostListView(ListView):
    """This class create the list view on the main page, also sorted the posts from by the 
    date from newest to oldest. 

    Args:
        ListView (Django.views object): The list view from django
    """
    model = Post
    template_name = 'blog/home.html' # <app>/<model>_<viewtype>.html
    context_object_name = 'posts'
    ordering = ['-date_posted'] # order the ho


class PostDetailView(DetailView):
    """This class create the list view on the main page, also sorted the posts from by the 
    date from newest to oldest. 

    Args:
        ListView (Django.views object): The list view from django
    """
    model = Post


class PostCreateView(LoginRequiredMixin, CreateView):
    """The View to create new post 

    Args:
        CreateView (CreateView): The django creative view package
    """
    model = Post
    # We only wish to modify title and content
    fields =['title', 'content']
    def form_valid(self, form: BaseModelForm) -> HttpResponse:
        form.instance.author = self.request.user #Route the author to the current login user
        return super().form_valid(form)
    

class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    """_summary_

    Args:
        LoginRequiredMixin (_type_): _description_
        UserPassesTestMixin (_type_): _description_
        UpdateView (_type_): _description_

    Returns:
        _type_: _description_
    """
    model = Post
    # We only wish to modify title and content
    fields =['title', 'content']

    def form_valid(self, form: BaseModelForm) -> HttpResponse:
        form.instance.author = self.request.user #Route the author to the current login user
        return super().form_valid(form)
    
    def test_func(self):
        # get the current post project
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False
    

class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
   
    model = Post
    success_url = '/'
    def test_func(self):
        """Test fuction if the user trying yo modified the post is the same as the login user

        Returns:
            bool: If the user passed the user test(Only)
        """
        # get the current post project
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False

def about(request):
    return render(request, 'blog/about.html')