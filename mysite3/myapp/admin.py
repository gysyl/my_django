from django.contrib import admin

# Register your models here.
from .models import MyUser
class MyUserAdmin(admin.ModelAdmin):
    list_display = ('id', 'username', 'created_at')
    list_display_links = ('id', 'username')
    search_fields = ('username',)
    list_filter = ('created_at',)
    #list_editable = ('password',)
    #ordering = ('-created_at',)
    #list_per_page = 10
admin.site.register(MyUser, MyUserAdmin)
