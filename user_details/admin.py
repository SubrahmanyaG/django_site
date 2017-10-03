from django.contrib import admin
from django.utils.html import format_html
from .models import  UserDetails
# Register your models here.


class UserDetailsAdmin(admin.ModelAdmin):
    list_display = ['person', ]
    list_filter= ['state', 'person', 'created_at']
admin.site.register(UserDetails, UserDetailsAdmin)