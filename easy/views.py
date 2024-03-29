from django.shortcuts import render, HttpResponse,redirect
from .models import Contact, Sinup
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
import requests
import json
from django.core.mail import send_mail
import random
from django.conf import settings
from simplejson import JSONDecodeError

# Create your views here.
def bussiness(request):
    #bussiness_api_request = requests.get('http://newsapi.org/v2/top-headlines?country=us&category=business&apiKey=16b2973603f04e4eac23d452bc0d40fb')
    bussiness_api_request = requests.get('https://newsapi.org/v2/top-headlines?country=us&category=business&apiKey=bd21a406a18442f684b1bfd1f3bad0df')
    bussiness_api = json.loads(bussiness_api_request.content)
    return render(request, 'bussiness.html', {'bussiness_api': bussiness_api})
def loginhandle(request):
    if request.method == "POST":
        email = request.POST['email']
        loginpassword = request.POST['loginpassword']
        loginusername = User.objects.get(email=email.lower()).username
        # create a authetication
        user = authenticate(username=loginusername, password=loginpassword)
        # a backend authetication
        if user is not None:
            login(request, user)
            messages.success(request,'you login successfully')
            return redirect("/")
        else:
            messages.warning(request, "please entre correct password and email")
            return render(request, 'login.html')
    return render(request, 'login.html')
def logouthandle(request):
    logout(request)
    messages.success(request,'you suceesfully logout')
    return redirect('login')

def sinup(request):
    if request.method == "POST":
        name = request.POST['name']
        username = request.POST['username']
        email = request.POST['email']
        phone = request.POST['phone']
        password = request.POST['password']
        #if not username.isalnum():
         #   messages.warning(request, "name should contain only alphabet")
        #if username.isalnum():
          #  messages.warning(request, "please entre correct username with numbers")
           # return redirect('sinup')
        if len(phone) != 10:
            messages.warning(request, "entre correct phone number")
            return redirect('sinup')
        if len(password) < 5:
            messages.warning(request,"entre strong password")
            return redirect('sinup')
        if User.objects.filter(username__iexact=username).exists():
            messages.warning(request, "Entre another usernmae this was taken")
            return redirect('sinup')

        # rechapcha
        clientkey = request.POST['g-recaptcha-response']
        secretkey = '6Lf6H20aAAAAAE1ZPPqFCRJYnJpAVn9C4paWjCNv'
        capthacaData = {
            'secret': secretkey,
            'response': clientkey
        }
        r = requests.post('https://www.google.com/recaptcha/api/siteverify ', data=capthacaData)
        #response = json.loads(r.text)
        #verify = response['success']
        #print('your sucess is', verify)


        messages.success(request, 'Your are sinup now!')

        # create the user
        myuser = User.objects.create_user(username, email, password)
        myuser.phone = phone
        myuser.name = name
        messages.success(request, "Now you can login yourself")
        sinup = Sinup(name=name, email=email, phone=phone,username=username)
        sinup.save()
        return redirect('login')
    else:
        return render(request, 'sinup.html')



def contact(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        text = request.POST.get('text')
        if len(phone) != 10:
            messages.warning(request,'please entre correct phone number')
            return redirect('contact')
        """
        if not name.isalnum():
            messages.warning(request, "name should contain only alphabet")
            return redirect('contact')
            
        if request.user.is_anonymous:
            messages.warning(request, "please first login yourself")
            return redirect("/login")

        """
        contact = Contact(name=name, email=email, phone=phone, text=text)
        contact.save()
        messages.success(request, 'Your message has been sent!')
        return redirect("/")

    return render(request, 'contact.html')
def news(request):
    #news_api_request = requests.get("http://newsapi.org/v2/top-headlines?sources=techcrunch&apiKey=16b2973603f04e4eac23d452bc0d40fb")
    news_api_request = requests.get("https://newsapi.org/v2/top-headlines?sources=techcrunch&apiKey=bd21a406a18442f684b1bfd1f3bad0df")

    api = json.loads(news_api_request.content)
    return render(request, 'news.html', {'api': api})
def index(request):
    indian_api_request = requests.get('http://newsapi.org/v2/top-headlines?country=in&apiKey=16b2973603f04e4eac23d452bc0d40fb')
    indian_api = json.loads(indian_api_request.content)
    return render(request, 'index.html', {'indian_api': indian_api})

def Entertainment(request):
    Entertainment_api_request = requests.get('https://newsapi.org/v2/top-headlines?country=in&category=entertainment&apiKey=bd21a406a18442f684b1bfd1f3bad0df')
    Entertainment_api = json.loads(Entertainment_api_request.content)
    return render(request, 'topheadlines.html', {'Entertainment_api': Entertainment_api})

def sports(request):
    sports_api_request = requests.get('https://newsapi.org/v2/top-headlines?country=in&category=sports&apiKey=bd21a406a18442f684b1bfd1f3bad0df')
    sports_api = json.loads(sports_api_request.content)
    return render(request, 'sports.html', {'sports_api': sports_api})

def health(request):
    health_api_request = requests.get('https://newsapi.org/v2/top-headlines?country=in&category=health&apiKey=bd21a406a18442f684b1bfd1f3bad0df')
    health_api = json.loads(health_api_request.content)
    return render(request, 'health.html', {'health_api': health_api})

def science(request):
    science_api_request = requests.get('https://newsapi.org/v2/top-headlines?country=in&category=science&apiKey=bd21a406a18442f684b1bfd1f3bad0df')
    science_api = json.loads(science_api_request.content)
    return render(request, 'science.html', {'science_api': science_api})