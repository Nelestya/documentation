from django.contrib import admin

# Register your models here.
from .models import *



class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')
    list_filter = ('name',)
    search_fields = ('name', 'description')
    prepopulated_fields = {'slug': ('name',)}

admin.site.register(Category, CategoryAdmin)

class DocumentationAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'author', 'created', 'updated',)
    list_filter = ('category',)
    search_fields = ('name', 'author')
    ordering = ('updated', 'name', 'category', 'author')


admin.site.register(Documentation, DocumentationAdmin)

class CopyrightAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'created', 'updated',)
    list_filter = ('name',)


admin.site.register(Copyright, CopyrightAdmin)
