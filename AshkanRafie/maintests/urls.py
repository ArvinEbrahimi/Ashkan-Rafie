from django.urls import path
from . import views

app_name = 'tests'

urlpatterns = [
    path('',views.tests_page,name='tests_page')
]