from django.contrib import messages
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.models import Group, Permission
from django.http import HttpResponseRedirect
from django.shortcuts import render

# from user.forms import SignUpForm, UserUpdateForm, ProfileUpdateForm
from django.urls import reverse

from company.models import Company
from user.forms import SignUpForm, CompanySignUpForm, ForgetPasswordForm
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


def company_login_form(request):
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
            return HttpResponseRedirect('/company-login')
    # Return an 'invalid login' error message.
    context = {  # 'category': category
    }
    return render(request, 'company-login.html', context)


def signup_form(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()  # completed sign up
            login(request, user, backend='django.contrib.auth.backends.ModelBackend')
            group = Group.objects.get(name='job_seeker')
            group.user_set.add(user)
            permissions = group.permissions.all()
            for p in permissions:
                user.user_permissions.add(p)

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


def company_signup_form(request):
    if request.method == 'POST':
        form = CompanySignUpForm(request.POST)
        if form.is_valid():
            user = form.save()  # completed sign up
            login(request, user, backend='django.contrib.auth.backends.ModelBackend')
            group = Group.objects.get(name='employer')
            group.user_set.add(user)
            permissions = group.permissions.all()
            for p in permissions:
                user.user_permissions.add(p)

            # Create data in profile table for user
            current_user = request.user
            data = Company()
            data.user_id = current_user.id
            data.slug = current_user.username
            data.auth_person = form.cleaned_data.get('first_name') + ' ' + form.cleaned_data.get('last_name')
            data.company_name = form.cleaned_data.get('company_name')
            data.email = form.cleaned_data.get('email')
            data.save()
            messages.success(request, 'Your account has been created!')
            return HttpResponseRedirect('/company-info/'+data.slug)
        else:
            messages.warning(request, form.errors)
            return HttpResponseRedirect('/company-signup')

    form = SignUpForm()
    # category = Category.objects.all()
    context = {  'form': form,
    }
    return render(request, 'company-signup.html', context)


def logout_func(request):
    logout(request)
    return HttpResponseRedirect('/')


@login_required(login_url='/login')  # Check login
def change_password(request):

    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Important!
            messages.success(request, 'Your password was successfully updated!')
            return HttpResponseRedirect('/user')
        else:
            messages.warning(request, 'Please correct the error below.<br>' + str(form.errors))
            return HttpResponseRedirect('/change-password')
    else:
        # category = Category.objects.all()
        form = PasswordChangeForm(request.user)
        context = {'form': form, }
        return render(request, 'change-password.html', context)


def forget_password(request):

    if request.method == 'POST':
        form = ForgetPasswordForm(request.user, request.POST)
        if form.is_valid():
            #??

            messages.success(request, 'Your password was successfully updated!')
            return HttpResponseRedirect('/user')
        else:
            messages.warning(request, 'Please correct the error below.<br>' + str(form.errors))
            return HttpResponseRedirect('/forget-password')
    else:
        # category = Category.objects.all()
        form = PasswordChangeForm(request.user)
        context = {'form': form, }
        return render(request, 'forget-password.html', context)

