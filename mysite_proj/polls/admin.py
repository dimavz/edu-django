from django.contrib import admin

# Register your models here.

from .models import Question, Choice

class ChoiseInline(admin.StackedInline):
    model = Choice
    extra =2

class QuestionAdmin(admin.ModelAdmin):
    fields = ['question_text','pub_date']
    inlines = [ChoiseInline]
    list_filter = ['pub_date']



admin.site.register(Question, QuestionAdmin)
#admin.site.register(Choice)
