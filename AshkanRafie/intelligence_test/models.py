from django.db import models
from account.models import User

class IntelligenceType(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name

class Question(models.Model):
    text = models.TextField()
    intelligence_type = models.ForeignKey(IntelligenceType, on_delete=models.CASCADE, related_name='questions')

    def __str__(self):
        return self.text

class AnswerChoice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='choices')
    text = models.CharField(max_length=255)
    score = models.IntegerField()  # نمره پاسخ

    def __str__(self):
        return self.text

class TestResult(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,related_name="intelligence_test_results")
    date_taken = models.DateTimeField(auto_now_add=True)
    results = models.JSONField()  # برای ذخیره نمرات هوش های مختلف، به عنوان مثال، {'زبان': 15, 'منطق': 20, ...}

    def __str__(self):
        return f"نتیجه آزمون {self.user.username} ({self.date_taken})"