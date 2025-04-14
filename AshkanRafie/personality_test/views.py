from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Question, AnswerChoice, TestResult, PersonalityType
from .forms import TestForm
from django.utils import timezone
import json

@login_required
def take_test(request):
    """
    نمایش فرم آزمون DISC به کاربر.
    """
    questions = Question.objects.all()
    form = TestForm()
    context = {'questions': questions, 'form': form}
    return render(request, 'personality_test/take_test.html', context)

@login_required
def process_test(request):
    """
    پردازش پاسخ های ارسالی کاربر، محاسبه نمرات DISC و ذخیره نتایج.
    """
    if request.method == 'POST':
        form = TestForm(request.POST)
        if form.is_valid():
            results = {}
            personality_types = PersonalityType.objects.all()
            for personality_type in personality_types:
                results[personality_type.name] = 0

            for question_id_str, answer_id_str in form.cleaned_data.items():
                if question_id_str.startswith('question_'):
                    try:
                        answer_id = int(answer_id_str)
                        answer = AnswerChoice.objects.get(id=answer_id)
                        question = answer.question
                        results[question.personality_type.name] += answer.score
                    except (ValueError, AnswerChoice.DoesNotExist):
                        print(f"Error: Invalid answer ID: {answer_id_str}")
                        return render(request, 'personality_test/error.html', {'message': 'پاسخ نامعتبر. لطفا دوباره امتحان کنید.'})

            test_result = TestResult.objects.create(
                user=request.user,
                results=results,
                date_taken=timezone.now()
            )

            # محاسبه نوع شخصیت غالب
            dominant_type = max(results, key=results.get)

            return redirect('personality_test:test_results', result_id=test_result.id, dominant_type=dominant_type)  # ارسال dominant_type به context

        else:
            return render(request, 'personality_test/take_test.html', {'form': form})
    else:
        return redirect('personality_test:take_test')

@login_required
def test_results(request, result_id, dominant_type):
    """
    نمایش نتایج آزمون DISC، از جمله نمرات و نوع شخصیت غالب.
    """
    result = get_object_or_404(TestResult, id=result_id, user=request.user)
    context = {'result': result, 'dominant_type': dominant_type}  # اضافه کردن dominant_type به context
    return render(request, 'personality_test/test_results.html', context)

@login_required
def latest_test_result(request):
    """
    نمایش آخرین نتیجه آزمون DISC کاربر.
    """
    try:
        result = TestResult.objects.filter(user=request.user).latest('date_taken')
        dominant_type = max(result.results, key=result.results.get) # محاسبه dominant type
        return redirect('personality_test:test_results', result_id=result.id, dominant_type=dominant_type)
    except TestResult.DoesNotExist:
        return render(request, 'personality_test/no_results.html')
@login_required
def detail(request):
    return render(request,'personality_test/exam_detail.html')