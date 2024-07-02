from django.urls import path
from . import views

app_name='weather'

urlpatterns = [
    path('', views.home, name='get_weather'),
    path('daily/<str:date>/', views.daily_detail_view, name='daily_detail_view'),
  
]