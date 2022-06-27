from django.shortcuts import render

# Create your views here.
from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView

from django.urls import reverse_lazy
from blog.models import Post



class PostListView(generic.ListView):
    model = Post

class PostCreateView(generic.CreateView):
    model = Post
    fields = “__all__”
    success_url  = reverse_lazy(“blog:all”)


class PostDetailview(generic.DetailView):
    model = Post

class PostUpdateView(generic.UpdateView):
    model = Post
    fields = “__all__”
    success_url  = reverse_lazy(“blog:all”)

class PostDeleteView(generic.UpdateView):
    model = Post
    fields = “__all__”
    success_url  = reverse_lazy(“blog:all”)

