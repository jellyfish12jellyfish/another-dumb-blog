from django.urls import path
from .views import home_view, PostListView, PostDetailView

app_name = 'blog'
urlpatterns = [
    path('', home_view, name='home_view'),
    path('posts/', PostListView.as_view(), name='post_list_view'),
    path('posts/<int:id>/', PostDetailView.as_view(), name='post_detail_view'),
]
