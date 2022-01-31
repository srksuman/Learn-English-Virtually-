from django.contrib import admin
from .models import Question, Answer, TestManagement, Result

class AnswerInline(admin.TabularInline):
    model = Answer

class QuestionAdmin(admin.ModelAdmin):
    inlines = [AnswerInline]

admin.site.register(Question, QuestionAdmin)
admin.site.register(Answer)
admin.site.register(TestManagement)
admin.site.register(Result)
