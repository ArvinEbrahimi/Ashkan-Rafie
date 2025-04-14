from django.contrib import admin
from .models import AnswerChoice,Question,TestResult,IntelligenceType
# Register your models here.

admin.site.register(AnswerChoice)
admin.site.register(Question)
admin.site.register(TestResult)
admin.site.register(IntelligenceType)


