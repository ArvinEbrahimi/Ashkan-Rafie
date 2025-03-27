from django.urls import path
from . import views

app_name = 'moshavere'

urlpatterns = [
    path('',views.moshavere_page,name='moshavere_page')
]