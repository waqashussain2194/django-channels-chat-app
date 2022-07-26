from django.contrib.auth.models import User
from django.shortcuts import render
from .models import Thread
from django.http import Http404
from django.views.generic import View
# Create your views here.

def index(request):
    return render(request, 'chatApp/index.html')

def chatInterface(request):
    users = User.objects.all()
    return render(request, 'chatApp/chatInterface.html', {'users': users})


class ChatView(View):
    template_name = 'chatApp/chat.html'
    
    def get(self,request,username):
        return render(request, 'chatApp/chat.html')