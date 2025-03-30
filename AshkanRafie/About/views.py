from django.shortcuts import render
from .models import Bio
# Create your views here.
def About_page(request):
    bio = Bio.objects.all()
    return render(request,"about/About.html",{'bio':bio})