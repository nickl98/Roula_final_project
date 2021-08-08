from django.contrib import admin


from .models import Question
# Register Team Model here.


class QuestionAdmin(admin.ModelAdmin):
    list_display = (
        'asked_by',
        'question_about',
        'answer',
        'answered_by',
        )
    ordering = ('asked_by',)


admin.site.register(Question, QuestionAdmin)
