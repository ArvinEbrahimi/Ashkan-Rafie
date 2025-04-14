from django.contrib import admin
from .models import Dimension,Question,AnswerChoice,TestResult
# Register your models here.

admin.site.register(Question)
admin.site.register(AnswerChoice)
admin.site.register(TestResult)
admin.site.register(Dimension)

