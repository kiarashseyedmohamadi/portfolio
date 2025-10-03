from django.contrib import admin
from .models import Comment

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('name', 'text', 'create_at', 'is_active')
    list_filter = ('is_active',)
    search_fields = ('name', 'text')

