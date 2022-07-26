from django.urls import path
from . import views
urlpatterns = [
    path('', views.register, name='chatApp-register'),
    path('login/', views.login, name='chatApp-login'),
    path('logout/', views.logout, name='chatApp-logout'),
    ]