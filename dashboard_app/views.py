from django.shortcuts import render
from django.urls import reverse
from django.http import HttpResponse, HttpResponseRedirect

from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.db import IntegrityError

from .models import User



# Create your views here.
@login_required(login_url='/login')
def index(request):
    return render(request, 'dashboard_app/index.html')


def login_view(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if not user:
            return render(request, 'dashboard_app/login.html', {
                "message": "Invalid Credentials"
            })

        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    
    return render(request, 'dashboard_app/login.html')


def signup(request):
    if request.method == "POST":
        username = request.POST['username']
        first_name = request.POST['firstname']
        last_name = request.POST['lastname']

        profile_pic = request.FILES.get('profilepic', None)

        email = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']

        role = request.POST['role']
        address = request.POST['address']

        if password != confirm_password:
            return render(request, 'dashboard_app/signup.html', {
                "message": "Password and Confirm Password didn't match"
            })
        
        try:
            user = User.objects.create_user(
                first_name = first_name,
                last_name = last_name,
                username = username, 
                email=email, 
                password=password,
                address = address,
                role=role,
            )
            if profile_pic:
                user.profile_pic = profile_pic
            user.save()

            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        except IntegrityError:
            return render(request, "dashboard_app/signup.html", {
                "message":"Username already taken."
            })

    return render(request, 'dashboard_app/signup.html')


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))