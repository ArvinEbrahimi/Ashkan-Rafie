from django import forms
from .models import Question, AnswerChoice

class TestForm(forms.Form):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        questions = Question.objects.all()
        for question in questions:
            choices = AnswerChoice.objects.filter(question=question)
            self.fields[f'question_{question.id}'] = forms.ChoiceField(
                label=question.text,
                choices=[(choice.id, choice.text) for choice in choices],
                widget=forms.RadioSelect,
                required=True,
            )
