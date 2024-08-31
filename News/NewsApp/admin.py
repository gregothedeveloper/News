from django.contrib import admin
from .models import Post

# Define the admin class for Post model

class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'status','author', 'created_at')
    search_field = ('author', 'status')
    list_filter = ('title', 'status','created_at')

# Register the Post model with the admin interface
# Register your models here.
admin.site.register(Post)