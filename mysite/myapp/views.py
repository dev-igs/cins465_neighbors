from django.shortcuts import render, redirect
from django.contrib.auth import logout, login
from django.http import HttpResponse

from . import forms
from . import models

#
# VIEWS FOR ACCOUNT
#

# LOGIN VIEWS
def logout_view(request):
    logout(request)
    return redirect('/login/')
# REGISTER_VIEW
def register_view(request):
    if request.method == "POST":
        form_instance = forms.RegistrationForm(request.POST)
        if form_instance.is_valid():
            user = form_instance.save()
            # login(request, user)
            return redirect("/login/")
    else:
        form_instance = forms.RegistrationForm()

    context = {
        "title":"Registration",
        "form":form_instance
    }
    return render(request, "auth/register.html", context=context)
#SIGN-ON
def signon(request):
    content = models.FormsModel.objects.all()
    context = {
        "title":"Project Website",
        "course":"CINS465",
        "text":"Hello World",
    }
    return render(request,"auth/signon.html", context=context)

#INDEX VIEWS
def index(request):
    if request.method == "POST":
        reply_form = forms.ReplyForms(request.POST)
        if reply_form.is_valid():
            reply_form.save()  #save data
            reply_form = forms.ReplyForms() #create instance
    else:
        reply_form = forms.ReplyForms()
    content = models.FormsModel.objects.all()
    context = {
        "title":"Project",
        "course":"CINS465",
        "text":"Hello World",
        "form":reply_form,
    }
    return render(request,"index.html", context=context)

# FEED VIEW
def feed(request):
    context = {
        "title":"Project",
        "course":"CINS465",
        "text":"Hello World",
    }
    return render(request,"feed.html", context=context)
