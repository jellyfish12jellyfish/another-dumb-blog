from django.contrib import admin
from .models import Post


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'status')
    list_filter = ('status','title',)
    search_fields = ('title', 'body')
    ordering = ('status',)
