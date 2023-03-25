from django.urls import path
from . import views


app_name = 'calcul'
urlpatterns = [
    path('', views.index, name='index'),
    path('calculate/<int:num1>/<int:num2>/', views.calculate, name='calculate'),
]
