from django.contrib import messages
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.models import Group, Permission, User
from django.db.models import Q
from django.http import HttpResponseRedirect
from django.shortcuts import render
from company.models import Company
from user.forms import SignUpForm, CompanySignUpForm, ForgetPasswordForm
from user.models import UserProfile
from django.shortcuts import render, redirect
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse
from django.contrib.auth.forms import PasswordResetForm
from django.contrib.auth.models import User
from django.template.loader import render_to_string
from django.db.models.query_utils import Q
from django.utils.http import urlsafe_base64_encode
from django.contrib.auth.tokens import default_token_generator
from django.utils.encoding import force_bytes


@login_required(login_url='/login')  # Check login
def index(request):
    return render(request, 'login.html')


def login_form(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None and user.has_perm('user.add_userprofile'):
            login(request, user)
            messages.success(request, "Başarılı bir şekilde giriş yapıldı")
            return HttpResponseRedirect('/')

        else:
            messages.warning(request, "Kullanıcı adı veya şifre hatalıdır")
            return HttpResponseRedirect('/login')

    return render(request, 'login.html')


def company_login_form(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)

        if user is not None and user.has_perm('company.add_company'):
            login(request, user)
            messages.success(request, "Başarılı bir şekilde giriş yapıldı")
            return HttpResponseRedirect('/')
        else:
            messages.warning(request, "Kullanıcı adı veya şifre hatalıdır")
            return HttpResponseRedirect('/company-login')

    return render(request, 'company-login.html')


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
            messages.success(request, "Kaydınız başarı ile tamamlandı")
            return HttpResponseRedirect('/create-resume')
        else:
            messages.warning(request, form.errors)
            return HttpResponseRedirect('/signup')

    return render(request, 'signup.html')


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

            current_user = request.user
            data = Company()
            data.user_id = current_user.id
            data.slug = current_user.username
            data.auth_person = form.cleaned_data.get('first_name') + ' ' + form.cleaned_data.get('last_name')
            data.company_name = form.cleaned_data.get('company_name')
            data.email = form.cleaned_data.get('email')
            data.save()
            messages.success(request, "Kaydınız başarı ile tamamlandı")
            return HttpResponseRedirect('/company-signup')
        else:
            messages.warning(request, form.errors)
            print(form.errors)
            return HttpResponseRedirect('/signup')

    return render(request, 'company-signup.html')


def logout_func(request):
    logout(request)
    messages.success(request, "Çıkış yapıldı")
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
        form = ForgetPasswordForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data['email']
            associated_users = User.objects.filter(Q(email=data))
            if associated_users.exists():
                for user in associated_users:
                    subject = "Password Reset Requested"
                    email_template_name = "user/templates/password_reset_email.txt"
                    c = {
                        "email": user.email,
                        'domain': '127.0.0.1:8000',
                        'site_name': 'Website',
                        "uid": urlsafe_base64_encode(force_bytes(user.pk)),
                        "user": user,
                        'token': default_token_generator.make_token(user),
                        'protocol': 'http',
                    }
                    email = render_to_string(email_template_name, c)
                    try:
                        send_mail(subject, email, 'ihsahin63@gmail.com', [user.email], fail_silently=False)
                    except BadHeaderError:
                        return HttpResponse('Invalid header found.')
                    return redirect("/")

            messages.success(request, 'Your password was successfully updated!')
            return HttpResponseRedirect('/')
        else:
            messages.warning(request, 'Please correct the error below.<br>' + str(form.errors))
            return HttpResponseRedirect('/forget-password')

    form = PasswordChangeForm(request.user)
    context = {'form': form, }
    return render(request, 'forget-password.html', context)


@login_required(login_url='/login') # Check login
def user_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Important!
            messages.success(request, 'Şifreniz başarıyla güncellendi')
            return HttpResponseRedirect('/')
        else:
            messages.error(request, str(form.errors))
            return HttpResponseRedirect('/change-password')
    else:
        form = PasswordChangeForm(request.user)
        return render(request, 'change-password.html', {'form': form})
