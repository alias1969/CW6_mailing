from django.contrib import admin

from blogs.models import Blog


@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'title',
        'content',
        'image',
        'count_views',
        'publication_at',
        'is_published',
    )
    list_filter = ('title', 'count_views', 'publication_at')
    search_fields = ('title', 'publication_at')