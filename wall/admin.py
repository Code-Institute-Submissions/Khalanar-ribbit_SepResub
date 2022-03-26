from django.contrib import admin
from .models import Post, Comment, Category, Profile

# Register your models here.
admin.site.register(Comment)
admin.site.register(Category)
admin.site.register(Profile)

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    '''ds'''
    prepopulated_fields = {'slug': ('title',)}
    list_filter = ('category', 'date_created')
    list_display = ('title', 'slug', 'category', 'date_created')
    search_fields = ['title', 'content']