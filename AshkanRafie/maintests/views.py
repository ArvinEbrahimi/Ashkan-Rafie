from django.shortcuts import render

# Create your views here
def tests_page(request):
    return render(request,'maintests/azmoon.html')
