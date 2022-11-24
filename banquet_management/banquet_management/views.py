"""
File contains functions of projects url requests
"""

from admins_work.forms import UserForm, UserProfileForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect


def home(request):
    """
    Used to render the home page
    :param request:
    :return:
    """
    return render(request, "Home.html", {})


def login_form(request):
    """
    Used to authenticate user so that he can login
    :param request:
    :return:
    """
    after_login = ""

    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user_credentials = authenticate(username=username, password=password)
        if user_credentials is not None:
            login(request, user_credentials)
            if after_login == "":
                return redirect("user_index")
            else:
                return HttpResponseRedirect(after_login)
    return render(request, "login_form.html", {})


def signup_form(request):
    """
    Used to register user
    :param request:
    :return:
    """
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        email = request.POST['email']

        user_form = UserForm(data=request.POST)
        user_profile_form = UserProfileForm(data=request.POST)
        if user_form.is_valid():
            new_form1 = User.objects.create_user(username=username,
                                                 password=password,
                                                 first_name=firstname,
                                                 last_name=lastname,
                                                 email=email)

            if user_profile_form.is_valid():
                new_user_profile_form = user_profile_form.save(commit=False)
                new_user_profile_form.user = new_form1
                new_user_profile_form.save()
                return redirect("login_form")
            else:
                print("user_profile_form not valid")
    return render(request, "Signup_form.html", {})


@login_required
def logout_user(request):
    """
    Called when user requests for logout
    :param request:
    :return:
    """
    logout(request)
    return redirect("HomePage")
