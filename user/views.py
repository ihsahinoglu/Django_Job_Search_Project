from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render

# from user.forms import SignUpForm, UserUpdateForm, ProfileUpdateForm
from user.forms import SignUpForm
from user.models import UserProfile


@login_required(login_url='/login')  # Check login
def index(request):
    current_user = request.user  # Access User Session information
    # profile = UserProfile.objects.get(user_id=current_user.id)

    return render(request, 'login.html')


def login_form(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            # current_user = request.user
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
            user = form.save()  # completed sign up
            login(request, user, backend='django.contrib.auth.backends.ModelBackend')

            # Create data in profile table for user
            current_user = request.user
            data = UserProfile()
            data.user_id = current_user.id
            data.first_name = form.cleaned_data.get('first_name')
            data.last_name = form.cleaned_data.get('last_name')
            data.save()
            messages.success(request, 'Your account has been created!')
            return HttpResponseRedirect('/create-resume')
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
