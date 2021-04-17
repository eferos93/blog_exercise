from django.shortcuts import render
from django.urls import reverse_lazy
from django.utils import timezone
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import (TemplateView, ListView,
                                  DetailView, CreateView, UpdateView, DeleteView)

# Create your views here.
from blog.forms import PostForm
from blog.models import Post


class AboutView(TemplateView):
    template_name = 'blog/about.html'


class PostListView(ListView):
    model = Post

    def get_queryset(self):
        return Post.objects \
            .filter(published_date__lte=timezone.now()) \
            .order_by('-published_date')


class PostDetailView(DetailView):
    model = Post


class PostCreateView(CreateView, LoginRequiredMixin):
    model = Post
    login_url = '/login/'
    redirect_field_name = 'blog/post_detail.html'
    form_class = PostForm


class PostUpdateView(UpdateView, LoginRequiredMixin):
    login_url = '/login/'
    redirect_field_name = 'blog/post_detail.html'
    form_class = PostForm
    model = Post


class PostDeleteView(LoginRequiredMixin, DeleteView):
    model = Post
    success_url = reverse_lazy('post_list')


class DraftListView(LoginRequiredMixin, ListView):
    login_url = '/login/'
    redirect_field_name = 'blog/post_list.html'
    model = Post

    def get_queryset(self):
        return Post.objects\
            .filter(published_date__isnull=True)\
            .order_by('created_date')