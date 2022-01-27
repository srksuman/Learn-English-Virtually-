from django.contrib import admin
from .models import * 
# Register your models here.


class AnswerTabularInline(admin.TabularInline):
    model = Answers

class QuestionAdmin(admin.ModelAdmin):
    inlines = [AnswerTabularInline]

admin.site.register(Questions,QuestionAdmin)
admin.site.register(TestManagement)
admin.site.register(Answers)
admin.site.register(Results)


