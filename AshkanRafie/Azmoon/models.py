from django.db import models
from account.models import User

class Question(models.Model):
    text = models.TextField()

    def __str__(self):
        return self.text

class AnswerChoice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='choices')
    text = models.CharField(max_length=255)
    dimension = models.CharField(max_length=2, help_text="e.g., IE, SN, TF, JP")
    score = models.IntegerField(default=0, help_text="Positive or negative score towards the dimension")

    def __str__(self):
        return self.text

class TestResult(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,related_name="azmoon_test_results")
    IE_score = models.IntegerField(default=0)
    SN_score = models.IntegerField(default=0)
    TF_score = models.IntegerField(default=0)
    JP_score = models.IntegerField(default=0)
    personality_type = models.CharField(max_length=4, blank=True, null=True)
    date_taken = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username}'s Result ({self.personality_type})"