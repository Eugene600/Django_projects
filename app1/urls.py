from . import views
from django.urls import path

urlpatterns = [
   path('articles/', views.articles), 
]
