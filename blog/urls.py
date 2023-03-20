from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name='index'),
    path('blogs',views.all_blogs.as_view(),name='allblogs'),
    path('blogs/<slug:slug>',views.blog_detail.as_view(),name='blog_detail'),
    path('read-later',views.ReadLater.as_view(),name="read-later")
]
    
