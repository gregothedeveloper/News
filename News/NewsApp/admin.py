from django.contrib import admin
from .models import Post,Author
from django.forms import Textarea
from django.db import models

# Define the admin class for Post model

class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'status','created_at')
    search_field = ('author', 'status','title')
    list_filter = ('author','created_at')
    formfield_overrides = {
        models.TextField:{
            'widget':Textarea(attrs={
                'rows': 5,
                'cols': 5,
            })
        }
    }
    # Add a custom action to publish selected posts
    def mark_as_completed(self, request, queryset):
        queryset.update(status=1)

    mark_as_completed.short_description = 'Mark as completed'
    actions = [mark_as_completed]

# Register the Post model with the admin interface
# Register your models here.
admin.site.register(Author)
admin.site.register(Post, PostAdmin)

# Admin Ui
admin.site.site_header = 'NEWS ARENA'
admin.site.site_title = 'Post App'