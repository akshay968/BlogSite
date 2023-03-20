from django.contrib import admin
from .models import Blog,Tag,Author,Comment


class BlogAdmin(admin.ModelAdmin):
    list_filter=("tags",'author',"date",)
    list_display=("title","date",'author',)
    prepopulated_fields={"slug":("title",)}

admin.site.register(Blog,BlogAdmin)
admin.site.register(Tag)
admin.site.register(Author)
admin.site.register(Comment)
