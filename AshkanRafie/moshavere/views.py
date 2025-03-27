from django.shortcuts import render
from .models import personalMoshavere,businessMoshavere,cardMoshavere

# Create your views here.
def moshavere_page(request):
    moshaverep = personalMoshavere.objects.all()
    moshavereb = businessMoshavere.objects.all() 
    card = cardMoshavere.objects.all()
    return render(request,"moshavere/moshavere.html",{'moshaverep':moshaverep,'moshavereb':moshavereb,'card':card})