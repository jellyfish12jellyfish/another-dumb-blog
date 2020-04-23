from django.shortcuts import render
from django.views.generic import ListView
from .models import Post


def home_view(request, *args, **kwargs):
    return render(request, 'base.html', {})


class PostListView(ListView):
    template_name = 'post/list_view.html'
    queryset = Post.published.all()

