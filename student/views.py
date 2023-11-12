from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import ContactModel
from .models import Sign_up 
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User

def home(request): 
    return render(request,"signup.html")

def service(request):
    return HttpResponse("thi id ervice")

def about(request):
    return HttpResponse("abouy")

def sign_up(request):
    if request.method =="POST":
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        cpassword = request.POST['cpassword']
        if User.objects.filter(email=email).exists():
            messages.error(request, "Email already exists")
            if password == cpassword:   
                user = User.objects.create_user(username  =username , email  =email, password = password)
                user.save()
                messages.success(request, "Details updated.")
                return render(request, "login.html")
            else:
                messages.error(request, "password doesnt match")
                return redirect("/sign_up/")
    else:
        return render(request,"signup.html")


def contact(request):
    if request.method =="POST":
        fname = request.POST['fname']
        lname = request.POST['lname']
        email = request.POST['email']
        phone = request.POST['phone']
        desc = request.POST['desc']
        c = ContactModel(fname = fname, lname = lname,email = email, phone = phone,desc = desc)
        c.save()
        messages.success(request, "Details updated.")
    return render(request,"contact.html")
    # return HttpResponse("contact")

def Login(request):
    if request.method == "POST":
        email = request.POST['email']
        password = request.POST['password']
        
        user = authenticate(request, email = email, password = password)
        if user is not None:
            login(request, user)
            return redirect("/service/")
        else:
            messages.error(request,"there is an error logging in")
    else:
        return render(request,"login.html")