from . import views
from django.urls import path

app_name = 'app1'

urlpatterns = [
   path('articles/', views.articles, name="list"), 
   path('articles/<slug:slug>/', views.article_detail, name='article_detail'),
]
