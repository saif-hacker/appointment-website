from django.shortcuts import render
from django.http import HttpResponse
from .models import ContactModel
from .models import Sign_up 

# Create your views here

def home(request):
    return render(request,"signup.html")

def service(request):
    return HttpResponse("thi id ervice")

def about(request):
    return HttpResponse("abouy")

def sign_up(request):
    if request.method =="POST":
        name = request.POST['name']
        email = request.POST['email']
        password = request.POST['password']
        cpassword = request.POST['cpassword']
        signup = Sign_up(name = name, email = email, password = password, cpassword = cpassword)
        signup.save()
        return HttpResponse("complete")
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
        return HttpResponse("data saved")
    else:
        return render(request,"contact.html")
    # return HttpResponse("contact")
