from django.urls import path,re_path
from . import views

app_name = "blog"

urlpatterns = [
    path('page/<int:page_num>/',views.blog_page,name='blog_page'),
    re_path(r'detail/(?P<slug>[-\w]+)/',views.blog_detail,name='blog_detail')
]