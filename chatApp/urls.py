from django.urls import path, re_path
from . import views
urlpatterns = [
    
    path('chat/', views.chatInterface, name='chatApp-Interface'),
    re_path(r'^chat/(?P<username>[\w.@+-]+)', views.ChatView.as_view(), name='chatApp-chat'),
    
    ]