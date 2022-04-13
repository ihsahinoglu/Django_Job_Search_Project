from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render

from company.models import Company
from home.forms import CreateResumeForm, CompanyInfoForm
from home.models import ContactMessage, Setting, ContactForm
from job.models import Job
from user.models import UserProfile, UserEducation, UserExperience, UserSkills


def index(request):
    setting = Setting.objects.get(id=1)
    populerCategories = Job.objects.all()
    page = "home"
    context = {'setting': setting,
               'page': page,
               'populerCategories': populerCategories,
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
    user_education = UserEducation.objects.filter(user_id=current_user.id)
    user_experience = UserEducation.objects.filter(user_id=current_user.id)
    print("burada")
    if request.method == 'POST':  # check post
        form = CreateResumeForm(request.POST, request.FILES, )
        print(form.errors)
        if form.is_valid():
            data = userprofile  # create relation with model
            data2 = UserEducation()
            data3 = UserExperience()
            data4 = UserSkills()
            if form.cleaned_data['image'] is not None:
                data.image = form.cleaned_data['image']
            data.birth_date = form.cleaned_data['birth_date']
            data.sex = form.cleaned_data['sex']
            data.city = form.cleaned_data['city']
            data.phone = form.cleaned_data['phone']
            data.email = form.cleaned_data['email']
            data.address = form.cleaned_data['address']
            data.web_site = form.cleaned_data['web_site']
            data.presentation = form.cleaned_data['presentation']

            data2.user = current_user
            data2.school = form.cleaned_data['school']
            data2.degree = form.cleaned_data['degree']
            data2.department = form.cleaned_data['department']
            data2.start_date = form.cleaned_data['start_date']
            data2.end_date = form.cleaned_data['end_date']
            data2.education_add_info = form.cleaned_data['education_add_info']

            data3.user = current_user
            data3.company = form.cleaned_data['company']
            data3.position = form.cleaned_data['position']
            data3.location = form.cleaned_data['location']
            data3.date_from = form.cleaned_data['date_from']
            data3.date_to = form.cleaned_data['date_to']
            data3.experience_add_info = form.cleaned_data['experience_add_info']

            data4.user = current_user
            data4.skill = form.cleaned_data['skill']
            data4.skill_value = form.cleaned_data['skill_value']
            print(data4.skill)
            print(form.cleaned_data['skill'])
            data.save()  # save data to table
            data2.save()
            data3.save()
            data4.save()
            # messages.success(request, "Your message has ben sent. Thank you for your message.")
            return HttpResponseRedirect('/')

    context = {'setting': setting,
               'userprofile': userprofile,
               'user_education': user_education,
               'user_experience': user_experience,
               }
    return render(request, 'create-resume.html', context)


def candidatesProfile(request):
    setting = Setting.objects.get(id=1)
    current_user = request.user
    userprofile = UserProfile.objects.get(user_id=current_user.id)
    user_education = UserEducation.objects.all().filter(user_id=current_user.id)
    user_experience = UserExperience.objects.all().filter(user_id=current_user.id)
    user_skills = UserSkills.objects.all().filter(user_id=current_user.id)
    print(user_skills)
    context = {'setting': setting,
               'userprofile': userprofile,
               'user_education': user_education,
               'user_experience': user_experience,
               'user_skills': user_skills
               }
    return render(request, 'candidates-profile.html', context)


# @login_required(login_url='/login')  # Check login
def companyInfo(request):
    setting = Setting.objects.get(id=1)
    current_user = request.user
    company = Company.objects.get(user_id=current_user.id)

    if request.method == 'POST':  # check post
        form = CompanyInfoForm(request.POST, request.FILES, )
        print(form.errors)
        if form.is_valid():
            data = company  # create relation with model
            if form.cleaned_data['logo'] is not None:
                data.logo = form.cleaned_data['logo']
            data.company_name = form.cleaned_data['company_name']
            data.sector = form.cleaned_data['sector']
            data.employers = form.cleaned_data['employers']
            data.city = form.cleaned_data['city']
            data.phone = form.cleaned_data['phone']
            data.email = form.cleaned_data['email']
            data.web_site = form.cleaned_data['web_site']
            data.address = form.cleaned_data['address']
            data.about_company = form.cleaned_data['about_company']

            data.save()  # save data to table

            # messages.success(request, "Your message has ben sent. Thank you for your message.")
            return HttpResponseRedirect('/')

    context = {'setting': setting,
               'company': company,
               }
    return render(request, 'company-info.html', context)
