from django.contrib import admin
from .models import Post

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'author', 'created_at')
    list_display_links = ('title',)
    search_fields = ('title', 'content', 'author__username')
    list_filter = ('created_at', 'author')
    readonly_fields = ('created_at',)
    ordering = ('-created_at',)
