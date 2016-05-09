from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.shortcuts import render, render_to_response
from Authentication.forms import LoginForm

def login(request):
    userid = ""
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            userid = form.cleaned_data["username"]
            passwd = form.cleaned_data["password"]
            user = authenticate(username=userid, password=passwd)
            if user is not None and user.is_active:
                return render(request, "index.html", {"username": userid})
            else:
                print "Invalid login."
    else:
        form = LoginForm()
    return render(request, "login.html", {"form": form, "username": userid})