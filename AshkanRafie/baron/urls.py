from django.urls import path
from . import views

app_name = 'eq_test'

urlpatterns = [
    path('take/', views.take_test, name='take_test'),
    path('process/', views.process_test, name='process_test'),
    path('results/<int:result_id>/', views.test_results, name='test_results'),
    path('results/latest/', views.latest_test_result, name='latest_test_result'),
    path('detail/', views.detail, name='detail_page'),
]