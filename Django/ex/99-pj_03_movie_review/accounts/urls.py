from django.urls import path
from . import views

app_name = 'accounts'
urlpatterns = [
    path('login/', views.login, name='login'),
    path('signup/', views.signup, name='signup'),
    path('logout/', views.logout, name='logout'),
    path('delete/', views.delete, name="delete"),
    path('profile/<int:user_pk>/', views.profile, name='profile'),
    path('profile/<int:user_pk>/update/', views.profile_update, name='profile_update'),
    path('password/', views.change_password, name='change_password'),
]