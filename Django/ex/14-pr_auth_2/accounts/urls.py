from django.urls import path
from . import views


app_name = 'accounts'
urlpatterns = [
    path('', views.hello, name='hello'),
    path('signup/', views.signup, name='signup'),
    path('update/', views.update, name='update'),
    path('delete/', views.delete, name='delete'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('password/', views.change_password, name='change_password'),
]