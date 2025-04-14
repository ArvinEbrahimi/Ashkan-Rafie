from django.db import models
from account.models import User

class PersonalityType(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name

class Question(models.Model):
    text = models.TextField()
    personality_type = models.ForeignKey(PersonalityType, on_delete=models.CASCADE, related_name='questions')

    def __str__(self):
        return self.text

class AnswerChoice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='choices')
    text = models.CharField(max_length=255)
    score = models.IntegerField()  # نمره پاسخ

    def __str__(self):
        return self.text

class TestResult(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,related_name="personality_results")
    date_taken = models.DateTimeField(auto_now_add=True)
    results = models.JSONField()  # برای ذخیره نمرات انواع شخصیت، به عنوان مثال، {'D': 15, 'I': 20, ...}

    def __str__(self):
        return f"نتیجه آزمون {self.user.username} ({self.date_taken})"
