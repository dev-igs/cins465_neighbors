from django.shortcuts import render, redirect
from django.contrib.auth import logout, login
#from django.http import HttpResponse

from . import models
from . import forms

# Create your views here.


######## ACCOUNT VIEWS START ###########
def logout_view(request):
    logout(request)
    return redirect('/login/')

def register_view(request):
    form_instance = forms.RegistrationForm(request.POST)
    if form_instance.is_valid():
        user = form_instance.save()
        #login(request, user)
        return redirect("/")
    else:
        form_instance = forms.RegistrationForm()

    context = {
        "title":"Registration",
        "form":form_instance
    }
    return render(request, "registration/register.html", context=context)

def account_view(request):
    context = {
        "title":"Account",
        "body":"Body",
    }
    return render(request, "account.html", context=context)


######## CHAT VIEWS START ###########
def chat_view(request):
    return render(request, 'chat/chat.html')

def chatroom_view(request, room_name):
    return render(request, 'chat/chatroom.html', {
        'room_name': room_name
    })

######## EVENTS VIEWS START ###########
def events_view(request):
    context = {
        "title":"Events",
        "body":"Body",
    }
    return render(request, "events.html", context=context)

######## RESOURCE VIEWS START ###########
def resource_view(request):
    context = {
        "title":"Resources",
        "body":"Body",
    }
    return render(request, "resources.html", context=context)

######## ABOUT VIEWS START ###########
def about_view(request):
    context = {
        "title":"About",
        "body":"Body",
    }
    return render(request, "about.html", context=context)
    #return HttpResponse("Hello All You People")

######## HOME/INDEX VIEWS START ###########
def index(request):
    context = {
        "title":"Neighbor",
        "body":"Body",
    }
    return render(request, "index.html", context=context)
    #return HttpResponse("Hello All You People")

