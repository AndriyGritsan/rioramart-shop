from django.contrib import admin
from .models import Post, Comment


# Register your models here.

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'slug', 'created_at')
    list_filter = ('created_at', )
    search_fields = ('title', 'content')
    prepopulated_fields = {'slug': ('title', )}
    readonly_fields = ('views', 'created_at', 'updated_at')
    
@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('id', 'post', 'name', 'created_at')
    list_filter = ('created_at', )
    search_fields = ('name', 'text')
    readonly_fields = ('created_at', )