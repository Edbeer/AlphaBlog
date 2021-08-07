from django.contrib import admin
from django import forms
from ckeditor_uploader.widgets import CKEditorUploadingWidget
from django.utils.safestring import mark_safe

from .models import *


class PostAdminForm(forms.ModelForm):
    content = forms.CharField(widget=CKEditorUploadingWidget())

    class Meta:
        model = Post
        fields = '__all__'


class PostAdmin(admin.ModelAdmin):
    form = PostAdminForm
    prepopulated_fields = {'slug': ('title',)}
    list_display = ('id', 'title', 'slug', 'views', 'created_at', 'get_photo',  'is_published')
    list_display_links = ('id', 'title', 'slug')
    readonly_fields = ('get_photo', 'views', 'created_at')
    fields = ('title', 'slug', 'content', 'photo', 'get_photo', 'created_at', 'views',  'is_published')
    list_filter = ('is_published',)
    list_editable = ('is_published',)
    search_fields = ('title',)
    save_on_top = True
    save_as = True

    def get_photo(self, obj):
        if obj.photo:
            return mark_safe(f'<img src="{obj.photo.url}" width="75">')

    get_photo.short_description = 'IMG'


class CommentAdmin(admin.ModelAdmin):
    form = PostAdminForm
    list_display = ('id', 'name', 'created_at')
    list_display_links = ('id', 'name',)
    readonly_fields = ('created_at',)
    search_fields = ('name',)


admin.site.register(Post, PostAdmin)
admin.site.register(Comment, CommentAdmin)


