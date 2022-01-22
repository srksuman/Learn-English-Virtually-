from django.contrib import admin

# Register your models here.
from .models import MainCotent
# Register your models here.
@admin.register(MainContent)
class MainContentAdmin(admin.ModelAdmin):
    list_display=['id','topic'.'sub_topic']