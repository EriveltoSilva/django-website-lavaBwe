from django.contrib import admin
from .models import FrequentQuestion, Team
from .models import Contact, Galeria, Carrocel

class ListFrequentQuestionAdmin(admin.ModelAdmin):
    list_display = ['id', "question", "author", "published","created_at",]
    list_display_links = ["id", "question", "created_at"]
    list_filter = ["id", "question", "author","created_at"]

    prepopulated_fields = {"slug":("question",)}

class ListTeamAdmin(admin.ModelAdmin):
    list_display = ['id', "name","num_hierarquical",  "published", "created_at",]
    list_display_links = ["id", "name","created_at"]
    list_filter = ["id", "name", "created_at"]

    prepopulated_fields = {"slug":("name",), "image_description":("name",)}




class ListContacts(admin.ModelAdmin):
    list_display = ('name', 'email','subject', 'created_at')
    list_display_links = ('name','email', )
    search_fields = ('name','email', 'created_at', )
    list_filter = ('name', 'email', 'created_at')
    list_per_page = 10

# class ListGaleries(admin.ModelAdmin):
#     list_display = ('id', 'title','published', 'created_at',)
#     list_display_links = ('id','title', 'created_at',)
#     search_fields = ('title','image_description', 'created_at', )
#     list_filter = ('title',  'created_at',)
#     list_per_page = 10

class ListCarrocel(admin.ModelAdmin):
    list_display = ('id', 'title','published', 'local','created_at',)
    list_display_links = ('id','title', 'local','created_at',)
    search_fields = ('title','local', 'published','created_at', )
    list_filter = ('title',  'local',)
    list_per_page = 10

admin.site.register(FrequentQuestion, ListFrequentQuestionAdmin)
admin.site.register(Team, ListTeamAdmin)
admin.site.register(Contact, ListContacts)
# admin.site.register(Galeria, ListGaleries)
admin.site.register(Carrocel, ListCarrocel)