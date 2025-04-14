from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Question, AnswerChoice, TestResult, IntelligenceType
from .forms import TestForm
from django.utils import timezone
import json

@login_required
def take_test(request):
    """
    نمایش فرم آزمون هوش چندگانه گاردنر به کاربر.
    """
    questions = Question.objects.all()
    form = TestForm()
    context = {'questions': questions, 'form': form}
    return render(request, 'intelligence_test/take_test.html', context)

@login_required
def process_test(request):
    """
    پردازش پاسخ‌های ارسالی کاربر، محاسبه نمرات هوش‌های چندگانه و ذخیره نتایج.
    """
    if request.method == 'POST':
        form = TestForm(request.POST)
        if form.is_valid():
            results = {}
            intelligence_types = IntelligenceType.objects.all()
            for intelligence_type in intelligence_types:
                results[intelligence_type.name] = 0

            for question_id_str, answer_id_str in form.cleaned_data.items():
                if question_id_str.startswith('question_'):
                    try:
                        answer_id = int(answer_id_str)
                        answer = AnswerChoice.objects.get(id=answer_id)
                        question = answer.question
                        results[question.intelligence_type.name] += answer.score
                    except (ValueError, AnswerChoice.DoesNotExist):
                        print(f"Error: Invalid answer ID: {answer_id_str}")
                        return render(request, 'intelligence_test/error.html', {'message': 'پاسخ نامعتبر. لطفا دوباره امتحان کنید.'})

            test_result = TestResult.objects.create(
                user=request.user,
                results=results,
                date_taken=timezone.now()
            )

            return redirect('intelligence_test:test_results', result_id=test_result.id)  # دیگر نیازی به ارسال dominant_type نیست

        else:
            return render(request, 'intelligence_test/take_test.html', {'form': form})
    else:
        return redirect('intelligence_test:take_test')

@login_required
def test_results(request, result_id):
    """
    نمایش نتایج آزمون هوش چندگانه گاردنر، شامل نمرات هر هوش.
    """
    result = get_object_or_404(TestResult, id=result_id, user=request.user)
    context = {'result': result}
    return render(request, 'intelligence_test/test_results.html', context)

@login_required
def latest_test_result(request):
    """
    نمایش آخرین نتیجه آزمون هوش چندگانه گاردنر کاربر.
    """
    try:
        result = TestResult.objects.filter(user=request.user).latest('date_taken')
        return redirect('intelligence_test:test_results', result_id=result.id)
    except TestResult.DoesNotExist:
        return render(request, 'intelligence_test/no_results.html')
    
@login_required
def detail(request):
    return render(request,'intelligence_test/exam_detail.html')