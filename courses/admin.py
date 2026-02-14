from django.contrib import admin
from .models import Course, Lesson, Question, Answer
from .models import TestAttempt, UserAnswer


class QuestionInline(admin.TabularInline):
    model = Question
    extra = 0


class CourseAdmin(admin.ModelAdmin):
    inlines = [QuestionInline]


class AnswerInline(admin.TabularInline):
    model = Answer
    extra = 0


class QuestionAdmin(admin.ModelAdmin):
    inlines = [AnswerInline]


admin.site.register(Course, CourseAdmin)
admin.site.register(Lesson)
admin.site.register(Question, QuestionAdmin)
admin.site.register(Answer)
admin.site.register(TestAttempt)
admin.site.register(UserAnswer)