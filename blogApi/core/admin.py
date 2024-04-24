from django.contrib import admin

from .models import Post

# Register your models here.
class PostAmin(admin.ModelAdmin):
    list_display = ['title', 'timestamp', 'updated']
    list_display_links = ['title']
    list_filter = ['timestamp']
    search_fields = ['title']
    class Meta:
        model = Post


admin.site.register(Post, PostAmin)