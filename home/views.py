from django.core.checks import messages
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render

# Create your views here.
from Django_Job_Search_Project import settings
from home.models import ContactMessage, Setting, ContactForm


def index(request):

    setting = Setting.objects.get(pk=1)
    page = "home"
    context = {'setting': setting,
               'page': page,
               #'products_slider': products_slider,
               #'products_latest': products_latest,
               #'products_picked': products_picked,
               # 'category':category
               }
    return render(request, 'index.html', context)


def contactus(request):
    # currentlang = request.LANGUAGE_CODE[0:2]
    # category = categoryTree(0,'',currentlang)
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
            #messages.success(request, "Your message has ben sent. Thank you for your message.")
            return HttpResponseRedirect('/contactus')

    #defaultlang = settings.LANGUAGE_CODE[0:2]
    #currentlang = request.LANGUAGE_CODE[0:2]
    setting = Setting.objects.get(pk=1)

    form = ContactForm
    context = {'setting':setting,
               'form': form}
    return render(request, 'contactus.html', context)
