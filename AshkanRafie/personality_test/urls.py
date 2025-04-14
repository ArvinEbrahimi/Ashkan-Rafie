from django.urls import path
from . import views

app_name = 'personality_test'


urlpatterns = [
    path('take/', views.take_test, name='take_test'),
    path('process/', views.process_test, name='process_test'),
    path('results/<int:result_id>/<str:dominant_type>/', views.test_results, name='test_results'), # Modified URL pattern
    path('results/latest/', views.latest_test_result, name='latest_test_result'),
    path('detail/', views.detail, name='detail_page'),
]