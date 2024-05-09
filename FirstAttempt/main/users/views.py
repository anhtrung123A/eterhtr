from django.shortcuts import render
from .forms import UserForm
from .models import User
from django.http import HttpResponseRedirect
from django.urls import reverse
# Create your views here.
def index(request):
    return render(request, "users/index.html")


def login(request):
    form = UserForm()
    context = {'form':form}
    if request.method == 'POST':
        user_name = request.POST['username']
        password = request.POST['password']
        if User.objects.filter(user_name = user_name):
            if password == User.objects.get(user_name = user_name).password:
                return HttpResponseRedirect(reverse("books:index"))
            else:
                return render (request, "users/login.html", {'error_message':'Incorrect password!'})
        else:
                return render (request, "users/login.html", {'error_message':'Username not found!'})
    return render (request, "users/login.html")


def registry(request):
    form = UserForm()
    context = {'form' : form}
    if request.method == 'POST':
        user_name = request.POST['username']
        password = request.POST['password']
        confirm_password = request.POST['confirm']
        if User.objects.filter(user_name=user_name):
            return render(request, "users/registry.html", {'error_message':"Account has already existed!"})
        else:
            if password == confirm_password:
                User(user_name = user_name, password = password).save()
            else:
                return render(request, "users/registry.html", {'error_message':"Passwords do not match"})
    return render(request, 'users/registry.html')
