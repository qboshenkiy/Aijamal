from django.contrib import admin
from .models import mainNews, cardNews

@admin.register(mainNews)
class mainNewsAdmin(admin.ModelAdmin):
    list_display = ('title', 'text', 'image')

@admin.register(cardNews)
class cardNewsAdmin(admin.ModelAdmin):
    list_display = ('datetime', 'category', 'image', 'title')

