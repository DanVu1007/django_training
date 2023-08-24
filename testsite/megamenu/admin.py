from django.contrib import admin

# Register your models here.
from .models import MegaMenu, MenuItem

class MegaMenuAdmin(admin.ModelAdmin):
    list_display = ('name', 'use_on_fe', 'banner')  # Add the fields you want to display

class MenuItemAdmin(admin.ModelAdmin):
    list_display = ('name', 'link', 'categories', 'content', 'show_categories', 'level_category', 'sequence')

admin.site.register(MegaMenu, MegaMenuAdmin)
admin.site.register(MenuItem, MenuItemAdmin)