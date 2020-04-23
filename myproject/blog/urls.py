from django.urls import path
from .views import home_view, PostListView

app_name = 'blog'
urlpatterns = [
    path('', home_view, name='home_view'),
    path('posts/', PostListView.as_view(), name='post_list_view'),
]
