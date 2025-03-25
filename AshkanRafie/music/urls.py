from django.urls import path,re_path
from . import views

app_name = "music"

urlpatterns = [
    path('',views.music_page,name='music_page'),
    path('page/<int:page_num>/',views.singletrack_page,name='singletrack_page'),
    re_path(r'detail/(?P<slug>[-\w]+)/',views.singletrack_detail,name='singletrack_detail')
]