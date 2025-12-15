from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView
from .models import BlogPost

class PostListView(ListView):
    model = BlogPost              
    template_name = 'blog/post_list.html'   
    context_object_name = 'posts'           


class PostDetailView(DetailView):
    model = BlogPost
    template_name = 'blog/post_detail.html'
    context_object_name = 'post'

class PostCreateView(CreateView):
    model = BlogPost
    fields = ['title', 'content']           
    template_name = 'blog/post_form.html'
    success_url = reverse_lazy('post_list') 

class PostUpdateView(UpdateView):
    model = BlogPost
    fields = ['title', 'content']
    template_name = 'blog/post_form.html'
    success_url = reverse_lazy('post_list')

