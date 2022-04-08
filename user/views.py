from django.contrib import messages
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import PasswordChangeForm
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render

from home.models import Setting
from job.models import Job
from company.models import Company
from user.forms import SignUpForm, UserUpdateForm, ProfileUpdateForm
from user.models import UserProfile


@login_required(login_url='/login')  # Check login
def index(request):
    current_user = request.user  # Access User Session information
    # profile = UserProfile.objects.get(user_id=current_user.id)

    return render(request, 'login.html')


def login_form(request):
    if request.method == 'POST':
        username = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            current_user = request.user
            # userprofile = UserProfile.objects.get(user_id=current_user.id)

            # Redirect to a success page.
            return HttpResponseRedirect('/')
        else:
            messages.warning(request, "Login Error !! Username or Password is incorrect")
            return HttpResponseRedirect('/login')
    # Return an 'invalid login' error message.

    context = {  # 'category': category
    }
    return render(request, 'login.html', context)


def signup_form(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()  # completed sign up

            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            email = form.cleaned_data.get('email')
            user = authenticate(username=username, password=password)
            login(request, user)
            # Create data in profile table for user
            current_user = request.user
            data = UserProfile(current_user.id)
            data.user_id = current_user.id
            data.image = "images/users/user.png"
            data.save()
            messages.success(request, 'Your account has been created!')
            return HttpResponseRedirect('/')
        else:
            messages.warning(request, form.errors)
            return HttpResponseRedirect('/signup')

    form = SignUpForm()
    # category = Category.objects.all()
    context = {  # 'category': category,
        'form': form,
    }
    return render(request, 'signup.html', context)

def logout_func(request):
    logout(request)
    return HttpResponseRedirect('/')
