from django.contrib import admin
from .models import Question,AnswerChoice,TestResult
# Register your models here.

admin.site.register(Question)
admin.site.register(AnswerChoice)
admin.site.register(TestResult)
