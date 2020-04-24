from django.contrib import admin
from .models import Post
from django import forms

from ckeditor_uploader.widgets import CKEditorUploadingWidget


class PostAdminForm(forms.ModelForm):
    body = forms.CharField(label=('Описание'), widget=CKEditorUploadingWidget())
    title=forms.CharField(label='Заголовок')

    class Meta:
        model = Post
        fields = '__all__'


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'status')
    list_filter = ('status', 'title',)
    search_fields = ('title', 'body')
    ordering = ('status',)
    form = PostAdminForm
