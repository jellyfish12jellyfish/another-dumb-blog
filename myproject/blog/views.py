from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView
from .models import Post


def home_view(request, *args, **kwargs):
    return render(request, 'base.html', {})


class PostListView(ListView):
    template_name = 'post/list_view.html'
    queryset = Post.published.all()

    model = Post
    context_object_name = 'pages'
    paginate_by = 2



class PostDetailView(DetailView):
    template_name = 'post/detail_view.html'

    def get_object(self):
        id_ = self.kwargs.get('id')
        return get_object_or_404(Post, id=id_)
