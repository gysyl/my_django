from django.contrib import admin
from . import models

class BookAdmin(admin.ModelAdmin):
    list_display = ('id','title', 'price', 'pub_house', 'market_price')
    list_display_links = ('id', 'title')
    search_fields = ('title','pub_house')
    list_filter = ('pub_house',)
    list_editable = ('price', 'market_price')
    #ordering = ('-price',)
    #list_per_page = 10

# Register your models here.
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('id','name', 'age', 'email')
    list_display_links = ('id', 'name')
    search_fields = ('name',)
    list_filter = ('age',)
    list_editable = ('email',)
    #ordering = ('-age',)
    #list_per_page = 10

admin.site.register(models.Book, BookAdmin)
admin.site.register(models.Author, AuthorAdmin)


