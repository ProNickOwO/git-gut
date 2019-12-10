from django.contrib import admin
from blog.models import Post
from.models import Post
from.models import Comment

#admin.site.register(Post)
# Register your models here.
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    last_display = ('title', 'slug', 'author', 'publish', 'status')
    list_filter = ('status','created','publish','author')
    search_fields = ('title','body')
    prepopulated_fields = {'slug':('title',)}
    raw_id_fields = ('author',)
    date_hierarchy = 'publish'
    ordering = ('status','publish')

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    last_display = ('name', 'email', 'post', 'created', 'active')
    list_filter = ('active','created','updated')
    search_fields = ('name','email','body')