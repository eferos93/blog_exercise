from django.shortcuts import render
from django.utils import timezone
from django.views.generic import (TemplateView, ListView)


# Create your views here.
from blog.models import Post


class AboutView(TemplateView):
    template_name = 'blog/about.html'


class PostListView(ListView):
    model = Post

    def get_queryset(self):
        return Post.objects\
            .filter(published_date__lte=timezone.now())\
            .order_by('-published_date')
