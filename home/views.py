from django.contrib.auth.decorators import login_required
from django.core.checks import messages
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render

from Django_Job_Search_Project import settings
from home.forms import CreateResumeForm
from home.models import ContactMessage, Setting, ContactForm
from job.models import Job
from user.models import UserProfile


def index(request):
    setting = Setting.objects.get(id=1)
    populerCategories = Job.objects.all()
    page = "home"
    context = {'setting': setting,
               'page': page,
               'populerCategories': populerCategories,
               # 'products_latest': products_latest,
               # 'products_picked': products_picked,
               # 'category':category
               }
    return render(request, 'index.html', context)


def contactus(request):
    if request.method == 'POST':  # check post
        form = ContactForm(request.POST)
        if form.is_valid():
            data = ContactMessage()  # create relation with model
            data.name = form.cleaned_data['name']  # get form input data
            data.email = form.cleaned_data['email']
            data.subject = form.cleaned_data['subject']
            data.message = form.cleaned_data['message']
            data.ip = request.META.get('REMOTE_ADDR')
            data.save()  # save data to table
            # messages.success(request, "Your message has ben sent. Thank you for your message.")
            return HttpResponseRedirect('/contactus')

    # defaultlang = settings.LANGUAGE_CODE[0:2]
    # currentlang = request.LANGUAGE_CODE[0:2]
    setting = Setting.objects.get(id=1)

    form = ContactForm
    context = {'setting': setting,
               'form': form}
    return render(request, 'contactus.html', context)


def jobDetails(request):
    setting = Setting.objects.get(id=1)
    job = Job.objects.get(id=1)

    # page = "home"
    context = {'setting': setting,
               # 'page': page,
               'job': job,
               }
    return render(request, 'job-details.html', context)


@login_required(login_url='/login')  # Check login
def createResume(request):
    setting = Setting.objects.get(id=1)
    current_user = request.user
    userprofile = UserProfile.objects.get(user_id=current_user.id)
    if request.method == 'POST':  # check post
        form = CreateResumeForm(request.POST, request.FILES,)
        if form.is_valid():
            data = userprofile  # create relation with model

            data.image = "images/users/" + str(form.cleaned_data['image'])
            data.birth_date = form.cleaned_data['birth_date']
            data.sex = form.cleaned_data['sex']
            data.city = form.cleaned_data['city']
            data.phone = form.cleaned_data['phone']
            data.email = form.cleaned_data['email']
            data.address = form.cleaned_data['address']
            data.web_site = form.cleaned_data['web_site']
            data.save()  # save data to table
            # messages.success(request, "Your message has ben sent. Thank you for your message.")
            return HttpResponseRedirect('/')

    context = {'setting': setting,
               'userprofile': userprofile,
               }
    return render(request, 'create-resume.html', context)


