from django import forms
from account.models import User
from django.core.exceptions import ValidationError


class SignUpForm(forms.Form):
    email = forms.EmailField(
        required=True,
        label="ایمیل",
        widget=forms.EmailInput(
            attrs={
                "class": "input",
                
            }
        ),
    )
    fullname = forms.CharField(
        required=True,
        label="نام و نام خانوادگی",
        widget=forms.TextInput(
            attrs={
                "class": "input",
                
            }
        ),
    )
    password = forms.CharField(
        required=True,
        label="رمز عبور",
        widget=forms.PasswordInput(
            attrs={
                "class": "input"
            }
        ),
    )
    confirm_password = forms.CharField(
        required=True,
        label="تایید رمز عبور",
        widget=forms.PasswordInput(
            attrs={
                "class": "input"
                
            }
        ),
    )


    class Meta:
        model = User
        fields = ["email", "password","fullname"]

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirm_password")
        if password != confirm_password:
            self.add_error("password", "رمز و تکرار آن باهم مطابقت ندارند")

    def save(self):
        email = self.cleaned_data["email"]
        password = self.cleaned_data["password"]
        fullname = self.cleaned_data["fullname"]
        user = User.objects.create_user(email=email, password=password, username=email ,first_name = fullname)
        return user


class LoginForm(forms.Form):

    email = forms.EmailField(
        required=True,
        label="ایمیل",
        widget=forms.EmailInput(
            attrs={"class": "input"}
        ),
    )
    password = forms.CharField(
        required=True,
        label="رمز عبور",
        widget=forms.PasswordInput(
            attrs={
                "class": "input",
                
            }
        ),
    )
