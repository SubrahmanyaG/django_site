from django.contrib import admin
from django.utils.html import format_html
from .models import  UserDetails
# Register your models here.


class UserDetailsAdmin(admin.ModelAdmin):
    list_display = ['person', 'display_photo']
    list_filter = ['state', 'person', 'created_at']

    def display_photo(self, obj):
        return '<img src="/static/{}" height="150", width="150" alt="Image">'.format(obj.image.name.split("/")[-1])

    display_photo.allow_tags = True
admin.site.register(UserDetails, UserDetailsAdmin)