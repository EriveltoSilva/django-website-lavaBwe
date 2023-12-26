from django.contrib import admin
from .models import Category, Post, Comment, NewletterAssinature


class ListCategories(admin.ModelAdmin):
    list_display = ('id', 'title', 'published', 'created_at')
    list_display_links = ('id', 'title', )
    search_fields =('title', 'summary', )
    list_filter = ('published', 'created_at', 'updated_at', )
    list_editable = ('published',)
    list_per_page = 10

    prepopulated_fields = {"slug":("title",)}

class ListPosts(admin.ModelAdmin):
    list_display = ('id', 'title', 'published','category','author', )
    list_display_links = ('id','title', 'author',)
    search_fields =('title', 'summary', 'content', 'image_thumb','author', 'created_at', 'updated_at',)
    list_filter = ('published', 'category', 'author','created_at','updated_at')
    list_editable = ('published',)
    list_per_page = 10

    prepopulated_fields = {"slug":("title",)}

class ListComments(admin.ModelAdmin):
    list_display = ('id', 'author', 'published', )    
    list_display_links = ('id', 'author', )
    search_fields =('author','content', 'created_at', 'updated_at',)
    list_filter = ('published', 'author','created_at','updated_at')
    list_editable = ('published',)
    list_per_page = 10

    prepopulated_fields = {"slug":("author",)}

class ListNewletterAssinatures(admin.ModelAdmin):
    list_display = ('id', 'name', 'email', 'created_at', )    
    list_display_links = ('id', 'name','email', )
    search_fields =('id', 'name','email', 'created_at',)
    list_filter = ('name','created_at')
    list_per_page = 10


admin.site.register(Category, ListCategories)
admin.site.register(Post, ListPosts)
admin.site.register(Comment, ListComments)
admin.site.register(NewletterAssinature, ListNewletterAssinatures)
