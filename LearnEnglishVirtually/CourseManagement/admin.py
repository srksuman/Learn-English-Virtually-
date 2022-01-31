from django.contrib import admin

# Register your models here.
from .models import MainContent,EnglishDictionary

# Register your models here.
@admin.register(MainContent)
class MainContentAdmin(admin.ModelAdmin):
    list_display=['id','topic']

# @admin.register(SubContent)
# class SubContentAdmin(admin.ModelAdmin):
#     list_display = ['id','sub_topic']

@admin.register(EnglishDictionary)
class EnglishDictionaryAdmin(admin.ModelAdmin):
    list_display=['word']