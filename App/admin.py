from .models import Question, Course
from django.contrib import admin


class QuestionAdmin(admin.ModelAdmin):
    list_display = ['question', 'course']
    search_fields = ['course']
    list_filter = ['course', 'question']
    ordering = ['course']


admin.site.register(Course)
admin.site.register(Question, QuestionAdmin)
