from django.contrib import admin

# Register your models here.
from .models import MainContent,SubContent
# Register your models here.
@admin.register(MainContent)
class MainContentAdmin(admin.ModelAdmin):
    list_display=['id','topic']

@admin.register(SubContent)
class SubContentAdmin(admin.ModelAdmin):
    list_display = ['id','topic','sub_topic']