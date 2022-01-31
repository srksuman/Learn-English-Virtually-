from django.contrib import admin
from .models import PreRegistration
# admin.site.site_header("Learn English Virtually")


# Register your models here.

@admin.register(PreRegistration)
class PreRegistrationAdmin(admin.ModelAdmin):
    list_display=['first_name','last_name']
