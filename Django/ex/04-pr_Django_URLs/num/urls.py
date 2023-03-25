from django.urls import path
from . import views

app_name = 'num'
urlpatterns = [
    path('', views.index, name='index'),
    path('number-print/<int:number>/', views.number_print, name='np'),
]
