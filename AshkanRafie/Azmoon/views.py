from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Question, AnswerChoice, TestResult
from django.utils import timezone # Import timezone
from .forms import TestForm

@login_required
def take_test(request):
    questions = Question.objects.all()
    form = TestForm()
    context = {'questions': questions, 'form': form}
    return render(request, 'exam/take_exam.html', context)

@login_required
def process_test(request):
    if request.method == 'POST':
        form = TestForm(request.POST)
        if form.is_valid():
            IE_score = 0
            SN_score = 0
            TF_score = 0
            JP_score = 0

            for question_id_str, answer_id_str in form.cleaned_data.items():
                if question_id_str.startswith('question_'):
                    try:
                        answer_id = int(answer_id_str)
                        answer = AnswerChoice.objects.get(id=answer_id)
                        if answer.dimension == 'IE':
                            IE_score += answer.score
                        elif answer.dimension == 'SN':
                            SN_score += answer.score
                        elif answer.dimension == 'TF':
                            TF_score += answer.score
                        elif answer.dimension == 'JP':
                            JP_score += answer.score
                    except (ValueError, AnswerChoice.DoesNotExist):
                        # Handle potential errors.  Log the error, or show a message to the user.
                        print(f"Error: Invalid answer ID: {answer_id_str}") # Log
                        return render(request, 'exam/exam_not_available.html', {'message': 'Invalid answer. Please retake the test.'})

            # Determine personality type based on scores (example logic)
            type_letters = ""
            type_letters += "I" if IE_score < 0 else "E"
            type_letters += "S" if SN_score < 0 else "N"
            type_letters += "T" if TF_score < 0 else "F"
            type_letters += "J" if JP_score < 0 else "P"

            # Use timezone.now()
            test_result = TestResult.objects.create(
                user=request.user,
                IE_score=IE_score,
                SN_score=SN_score,
                TF_score=TF_score,
                JP_score=JP_score,
                personality_type=type_letters,
                date_taken=timezone.now()
            )
            
            return redirect('exam:test_results', result_id=test_result.id) # Pass the ID

        else:
             # Form is invalid, re-render the page with errors
             return render(request, 'exam/take_exam.html', {'form': form})
    else:
        return redirect('exam:take_exam')

@login_required
def test_results(request, result_id):
    """Display a specific test result."""
    
    result = get_object_or_404(TestResult, id=result_id, user=request.user)  # Ensure user owns result
    if result.personality_type =="ISTJ":
        info = "منظم، مسئولیت‌پذیر و واقع‌گرا. به جزئیات توجه دارند و به اصول و قوانین پایبندند."
    elif result.personality_type =="ISFJ":
        info = "حامی و وفادار. به دیگران کمک می‌کنند و به احساسات و نیازهای دیگران توجه دارند."
    elif result.personality_type =="INFJ":
        info = "عمیق و بصیر. به ارزش‌ها و اصول انسانی اهمیت می‌دهند و تمایل به درک عمیق دیگران دارند."
    elif result.personality_type =="INTJ":
        info = "مستقل و تحلیل‌گر. به ایده‌ها و نظریه‌ها علاقه‌مندند و برنامه‌ریزی‌های بلندمدت می‌کنند."
    elif result.personality_type =="ISTP":
        info = "عملی و منطقی. به حل مشکلات و چالش‌ها علاقه دارند و معمولاً مهارت‌های فنی خوبی دارند."
    elif result.personality_type =="ISFP":
        info = "خلاق و حساس. به زیبایی‌ها و تجربیات حسی اهمیت می‌دهند و تمایل به زندگی در لحظه دارند."
    elif result.personality_type =="INFP":
        info = "ایده‌آل‌گرا و عاطفی. به ارزش‌ها و اصول خود پایبندند و به دنبال معنا در زندگی هستند."
    elif result.personality_type =="INTP":
        info = "منطقی و کنجکاو. به نظریه‌ها و ایده‌های جدید علاقه‌مندند و معمولاً تفکر تحلیلی قوی دارند."
    elif result.personality_type =="ESTP":
        info = "پر انرژی و عمل‌گرا. به تجربیات جدید علاقه‌مندند و معمولاً در موقعیت‌های چالش‌برانگیز خوب عمل می‌کنند."
    elif result.personality_type =="ESFP":
        info = "اجتماعی و خوش‌بین. به سرگرمی و لذت از زندگی اهمیت می‌دهند و معمولاً بسیار دوستانه هستند."
    elif result.personality_type =="ENFP":
        info = "خلاق و پرشور. به ایده‌های نوآورانه علاقه‌مندند و ارتباطات عاطفی عمیق برقرار می‌کنند."
    elif result.personality_type =="ENTP":
        info = "مبتکر و چالش‌طلب. به بحث و تبادل نظر علاقه دارند و معمولاً ایده‌های جدیدی را مطرح می‌کنند."
    elif result.personality_type =="ESTJ":
        info = "سازمان‌دهنده و کارآمد. به ساختار و نظم اهمیت می‌دهند و معمولاً رهبری قوی دارند."
    elif result.personality_type =="ESFJ":
        info = "اجتماعی و دلسوز. به نیازهای دیگران توجه دارند و معمولاً روابط اجتماعی قوی برقرار می‌کنند."
    elif result.personality_type =="ENFJ":
        info = "الهام‌بخش و دلسوز. به رشد دیگران اهمیت می‌دهند و معمولاً توانایی رهبری بالایی دارند."
    elif result.personality_type =="ENTJ":
        info = "قاطع و هدف‌گرا. به رهبری و سازمان‌دهی علاقه‌مندند و معمولاً در دستیابی به اهداف خود مصمم هستند."
    
    context = {'result': result,"info":info}


    
    return render(request, 'exam/exam_results.html', context)

@login_required
def latest_test_result(request):
    """Display the latest test result for the user."""
    try:
        result = TestResult.objects.filter(user=request.user).latest('date_taken')
        return redirect('exam:exam_results', result_id=result.id)
    except TestResult.DoesNotExist:
        return render(request, 'exam/exam_not_available.html')

@login_required
def detail(request):
    return render(request,'exam/exam_detail.html')