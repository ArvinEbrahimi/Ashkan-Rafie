from django.shortcuts import render

# Create your views here.


from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from .forms import SignUpForm, LoginForm
from .models import User
from . import forms



# Create your views here.

def sign_page(request):
    if request.method == "POST":
        form = SignUpForm(request.POST)
        print("2")
        if form.is_valid():
            print("1")
            email = form.cleaned_data.get("email")
            if User.objects.filter(email=email).exists():
                messages.add_message(
                    request, messages.ERROR, "این ایمیل قبلاً ثبت‌نام شده است."
                )
                return redirect("account:sign_page")
            else:
                messages.add_message(
                    request,
                    messages.SUCCESS,
                    "اکانت شما با موفقیت ساخته شد",
                )

                user = form.save()
                

                request.session["phone_number"] = user.email


                return redirect("home:home_page")
    else:
        form = SignUpForm()
    return render(request, "account/register.html", {"form": form})


def login_page(request):
    if request.user.is_authenticated:
        return redirect("home:home_page")
    else:
        form = forms.LoginForm()
        if request.method == "POST":
            form = forms.LoginForm(request.POST)
            if form.is_valid():
                user = User.objects.filter(email=form.cleaned_data.get("email")).first()
                password_check = user.check_password(form.cleaned_data.get("password"))
                if user == None or password_check == False:
                    messages.add_message(
                        request, messages.WARNING, "رمز یا ایمیل اشتباه است"
                    )
                else:
                        login(request, user)
                        messages.add_message(
                            request, messages.SUCCESS, "با موفقیت وارد شدید"
                        )
                        return redirect("home:home_page")
        return render(request, "account/login.html", context={"form": form})


def logout_page(request):
    logout(request)
    messages.add_message(request, messages.ERROR, "شما با موفقیت خارج شدید")
    return redirect("account:login_page")



