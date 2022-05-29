from django.contrib import messages
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.models import User
from django.db.models import Count, Q
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.utils import timezone
from django import template
from django.contrib.auth.models import Group
import user
from apply.models import Apply
from company.forms import ImageForm
from company.models import Company, CompanyPhotoGallery
from home import forms
from home.forms import CreateResumeForm, CompanyInfoForm, PostJobForm, SearchForm, ContactForm, EmployersSearchForm, \
    RateForm
from home.models import ContactMessage, Setting, FAQ
from home.other import CITY, CATEGORY, EDUCATION_LEVEL, EXPERIENCE, GENDER_, JOB_TYPE
from job.models import Job
from user.models import UserProfile, UserEducation, UserExperience, UserSkills
from django.forms import modelformset_factory, formset_factory


def index(request):
    setting = Setting.objects.get(id=1)
    recent_jobs = Job.objects.all().order_by('-create_at')[:8]

    popular_job_list = Apply.objects.order_by('job_id').values('job_id').distinct()
    popular_jobs = Job.objects.filter(id__in=popular_job_list)[:8]

    part_time_jobs = Job.objects.filter(job_type='Part-Time').order_by('-create_at')[:8]

    popular_categories = Job.objects.annotate(count=Count('category')).order_by('-count')
    popular_categories_dict = dict()
    for popular_category in popular_categories:
        popular_categories_dict[popular_category.category] = Job.objects.filter(
            category=popular_category.category).count()
    all_categories = Job.objects.values_list('category', flat=True).distinct()

    total_company = Company.objects.all().count()
    total_applications = Apply.objects.all().count()
    total_job = Job.objects.all().count()
    total_user = UserProfile.objects.all().count()
    if request.method == 'POST':
        form = SearchForm(request.POST)
        if form.is_valid():
            query_dict = {'category': form.cleaned_data['category'],
                          'city': form.cleaned_data['city'],
                          'query': form.cleaned_data['query'],
                          }
            request.method = 'GET'
            return jobList(request, **query_dict)

    context = {'setting': setting,
               'CITY': CITY,
               'popular_categories_dict': popular_categories_dict,
               'recent_jobs': recent_jobs,
               'popular_jobs': popular_jobs,
               'total_company': total_company,
               'total_applications': total_applications,
               'total_job': total_job,
               'total_user': total_user,
               'part_time_jobs': part_time_jobs,
               'all_categories': all_categories,
               }
    return render(request, 'index.html', context)


def contact(request):
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
            messages.success(request, "Mesajınız başarılı bir şekilde iletildi")
            return HttpResponseRedirect('/')
        else:
            messages.warning(request, form.errors)
    setting = Setting.objects.get(id=1)

    form = ContactForm
    context = {'setting': setting,
               'form': form}
    return render(request, 'contact.html', context)


def jobDetails(request, slug):
    setting = Setting.objects.get(id=1)
    job = Job.objects.get(slug=slug)
    current_user = request.user
    q = Apply.objects.values_list('user_id', flat=True).filter(job_id=job.id).distinct()
    applied_this_job = UserProfile.objects.filter(user_id__in=q)
    if request.method == 'POST':
        if request.user.groups.values_list('name', flat=True).first() == 'job_seeker':
            data = Apply()
            data.user_id = current_user.id
            data.job_id = job.id
            data.save()

            messages.success(request, "İlana başvuru yapıldı")
            return HttpResponseRedirect('/')
        else:
            messages.warning(request, "Sadece iş arayan statüsündeki kişiler başvuru yapabilir")
    context = {'setting': setting,
               'job': job,
               'applied_this_job': applied_this_job
               }
    return render(request, 'job-details.html', context)


@login_required(login_url='/login')
@permission_required('user.add_userprofile', login_url='/login')
def createResume(request):
    setting = Setting.objects.get(id=1)
    current_user = request.user
    userprofile = UserProfile.objects.get(user_id=current_user.id)
    user_education = UserEducation.objects.filter(user_id=current_user.id)
    user_experience = UserEducation.objects.filter(user_id=current_user.id)

    if request.method == 'POST':  # check post
        form = CreateResumeForm(request.POST, request.FILES, )
        if form.is_valid():

            data = userprofile
            if form.cleaned_data['image'] is not None:
                data.image = form.cleaned_data['image']
            data.birth_date = form.cleaned_data['birth_date']
            data.gender = form.cleaned_data['gender']
            data.city = form.cleaned_data['city']
            data.phone = form.cleaned_data['phone']
            data.email = form.cleaned_data['email']
            data.address = form.cleaned_data['address']
            data.title = form.cleaned_data['title']
            data.web_site = form.cleaned_data['web_site']
            data.presentation = form.cleaned_data['presentation']
            data.save()

            education_count = int(form.cleaned_data['educationCount'])
            school = request.POST.getlist('school')
            degree = request.POST.getlist('degree')
            department = request.POST.getlist('department')
            start_date = request.POST.getlist('start_date')
            end_date = request.POST.getlist('end_date')
            education_add_info = request.POST.getlist('education_add_info')
            for i in range(education_count):
                data2 = UserEducation()
                data2.user = current_user
                data2.school = school[i]
                data2.degree = degree[i]
                data2.department = department[i]
                data2.start_date = start_date[i]
                data2.end_date = end_date[i]
                data2.education_add_info = education_add_info[i]
                if data2.school and data2.degree and data2.department is not None:
                    data2.save()

            experience_count = int(form.cleaned_data['experienceCount'])
            company = request.POST.getlist('company')
            position = request.POST.getlist('position')
            location = request.POST.getlist('location')
            date_from = request.POST.getlist('date_from')
            date_to = request.POST.getlist('date_to')
            experience_add_info = request.POST.getlist('experience_add_info')
            for i in range(experience_count):
                data3 = UserExperience()
                data3.user = current_user
                data3.company = company[i]
                data3.position = position[i]
                data3.location = location[i]
                data3.date_from = date_from[i]
                data3.date_to = date_to[i]
                data3.experience_add_info = experience_add_info[i]
                if data3.company and data3.position is not None:
                    data3.save()

            skill_count = int(form.cleaned_data['skillCount'])
            skill = request.POST.getlist('skill')
            skill_value = request.POST.getlist('skill_value')
            for i in range(skill_count):
                data4 = UserSkills()
                data4.user = current_user
                data4.skill = skill[i]
                data4.skill_value = skill_value[i]
                if data4.skill and data4.skill_value is not None:
                    data4.save()

            messages.success(request, "Bilgileriniz başarıyla güncellendi")
            return HttpResponseRedirect('/')

        messages.warning(request, form.errors)
    context = {'setting': setting,
               'userprofile': userprofile,
               'user_education': user_education,
               'user_experience': user_experience,
               'CITY': CITY,
               }
    return render(request, 'create-resume.html', context)


def candidatesProfile(request, slug):
    setting = Setting.objects.get(id=1)
    current_user = User.objects.get(username=slug)
    userprofile = UserProfile.objects.get(user_id=current_user.id)
    user_education = UserEducation.objects.all().filter(user_id=current_user.id)
    user_experience = UserExperience.objects.all().filter(user_id=current_user.id)
    user_skills = UserSkills.objects.all().filter(user_id=current_user.id)
    applied = Apply.objects.values_list('job_id').filter(user_id=current_user.id)
    applied_jobs = Job.objects.filter(id__in=applied)
    jobs_for_me = Job.objects.filter(
        Q(title__icontains=userprofile.title) or Q(description__icontains=userprofile.title))
    print("rate:" + str(userprofile.rate))

    if request.method == 'POST':
        form = RateForm(request.POST)
        if form.is_valid():
            data = userprofile
            data.user = current_user
            new_rate = (userprofile.rate * userprofile.rate_count + int(form.cleaned_data['rate'])) \
                       / (userprofile.rate_count + 1)
            data.rate = round(new_rate,1)
            data.rate_count += 1
            data.save()
            messages.success(request, "Puanınız kaydedildi")
            request.method = 'GET'
            return candidatesProfile(request, slug)

    context = {'setting': setting,
               'userprofile': userprofile,
               'user_education': user_education,
               'user_experience': user_experience,
               'user_skills': user_skills,
               'applied_jobs': applied_jobs,
               'jobs_for_me': jobs_for_me
               }
    return render(request, 'candidates-profile.html', context)


@login_required(login_url='/login')
@permission_required('company.add_company', login_url='/login')
def companyInfo(request, slug):
    setting = Setting.objects.get(id=1)
    current_user = request.user
    company = Company.objects.get(slug=slug)

    if request.method == 'POST':  # check post
        form = CompanyInfoForm(request.POST, request.FILES, )

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

            messages.success(request, "Bilgileriniz kaydedildi")
            return HttpResponseRedirect('/')

    context = {'setting': setting,
               'company': company,
               'CITY': CITY,
               'CATEGORY': CATEGORY,
               }
    return render(request, 'company-info.html', context)


def companyDetail(request, slug):
    setting = Setting.objects.get(id=1)
    company = Company.objects.get(slug=slug)
    gallery = CompanyPhotoGallery.objects.filter(company_id=company.id)

    company_job = Job.objects.filter(company_id=company.id)
    form = ImageForm(request.POST, request.FILES)

    if request.method == "POST":
        if form.is_valid():
            for i in range(5):
                data = CompanyPhotoGallery()
                data.company = company
                s = 'image' + str(i + 1)
                if form.cleaned_data[s] is not None:
                    data.image = form.cleaned_data[s]
                    data.save()

            gallery = CompanyPhotoGallery.objects.filter(company_id=company.id)
            messages.success(request, "Fotoğraflar yüklendi")
            context = {'setting': setting,
                       'company': company,
                       'company_job': company_job,
                       'gallery': gallery,
                       }
            return render(request, 'company-detail.html', context)
        else:
            messages.warning(request, form.errors)

    context = {'setting': setting,
               'company': company,
               'company_job': company_job,
               'gallery': gallery,
               }
    return render(request, 'company-detail.html', context)


def jobList(request, **kwargs):
    setting = Setting.objects.get(id=1)
    all_categories = Job.objects.values_list('category', flat=True).distinct()
    query_dict = {'category': None,
                  'city': None,
                  'query': None,
                  'selected1': None,
                  'selected2': None,
                  'selected3': None,
                  'selected4': None,
                  'sort': None,
                  }
    for key, value in kwargs.items():
        if kwargs[key] is not "":
            query_dict[key] = value
    print(query_dict)

    def find_job(**query_dict):
        q = Q()
        if query_dict['category']:
            q &= Q(category=query_dict['category'])
        if query_dict['city']:
            q &= Q(city=query_dict['city'])
        if query_dict['query']:
            q2 = Q()
            q2 |= Q(title__icontains=query_dict['query'])  # search in title
            q2 |= Q(company__company_name__icontains=query_dict['query'])  # search in company name
            q2 |= Q(description__icontains=query_dict['query'])  # search in job description
            q &= q2
        if query_dict['selected1']:
            if query_dict['selected1'] == '1':  # filter by last 24 hours
                date_from = timezone.now() - timezone.timedelta(days=1)
                q &= Q(create_at__date__gte=date_from)
            if query_dict['selected1'] == '2':  # filter by last 1 week
                date_from = timezone.now() - timezone.timedelta(days=7)
                q &= Q(create_at__date__gte=date_from)
            if query_dict['selected1'] == '3':  # filter by last 1 mounth
                date_from = timezone.now() - timezone.timedelta(days=30)
                q &= Q(create_at__date__gte=date_from)

        if query_dict['selected2']:  # filter by education level
            q &= Q(education_level=query_dict['selected2'])

        if query_dict['selected3']:  # filter by experience level
            q &= Q(experience=query_dict['selected3'])

        if query_dict['selected4']:  # filter by gender
            q &= Q(gender=query_dict['selected4'])

        if query_dict['sort'] == 'descending':
            return Job.objects.filter(q).order_by('-create_at')[:20]
        if query_dict['sort'] == 'ascending':
            return Job.objects.filter(q).order_by('create_at')[:20]

        return Job.objects.filter(q).order_by('-create_at')[:20]

    job_list = find_job(**query_dict)

    if request.method == 'POST':
        form = SearchForm(request.POST)
        if form.is_valid():
            query_dict['query'] = form.cleaned_data['query']
            query_dict['city'] = form.cleaned_data['city']
            query_dict['category'] = form.cleaned_data['category']
            query_dict['selected1'] = form.cleaned_data['customRadio1']
            query_dict['selected2'] = form.cleaned_data['customRadio2']
            query_dict['selected3'] = form.cleaned_data['customRadio3']
            query_dict['selected4'] = form.cleaned_data['customRadio4']
            query_dict['sort'] = form.cleaned_data['sort']
            request.method = 'GET'
            return jobList(request, **query_dict)

    context = {'setting': setting,
               'job_list': job_list,
               'CITY': CITY,
               'all_categories': all_categories,
               'query_dict': query_dict,
               }
    return render(request, 'job-list.html', context)


@login_required(login_url='/company-login')
@permission_required('job.add_job', login_url='/company-login')
def PostJob(request):
    setting = Setting.objects.get(id=1)
    current_user = request.user
    company = Company.objects.get(user_id=current_user.id)
    # job = Job.objects.get(company_id=current_user.id)

    if request.method == 'POST':  # check post
        form = PostJobForm(request.POST)
        if form.is_valid():
            data = Job()  # create relation with model
            data.company_id = company.id
            data.title = form.cleaned_data['title']
            data.job_type = form.cleaned_data['job_type']
            data.category = form.cleaned_data['category']
            data.city = form.cleaned_data['city']
            data.gender = form.cleaned_data['gender']
            data.education_level = form.cleaned_data['education_level']
            data.experience = form.cleaned_data['experience']
            data.description = form.cleaned_data['description']

            data.save()  # save data to table

            messages.success(request, "İlanınız başarıyla oluşturuldu")
            return HttpResponseRedirect('/')
        messages.warning(request, form.errors)
    form = PostJobForm
    context = {'setting': setting,
               'form': form,
               'EDUCATION_LEVEL': EDUCATION_LEVEL,
               'EXPERIENCE': EXPERIENCE,
               'GENDER_': GENDER_,
               'CITY': CITY,
               'JOB_TYPE': JOB_TYPE,
               }
    return render(request, 'post-a-job.html', context)


def faq(request):
    setting = Setting.objects.get(id=1)
    faqs = FAQ.objects.all()
    context = {'setting': setting,
               'faqs': faqs,
               }
    return render(request, 'faq.html', context)


def about(request):
    setting = Setting.objects.get(id=1)
    context = {'setting': setting,
               }
    return render(request, 'about.html', context)


def employersList(request, **kwargs):
    setting = Setting.objects.get(id=1)
    query_dict = {'city': None,
                  'query': None,
                  'selected1': None,
                  'selected2': None,
                  'selected3': None,
                  'selected4': None,
                  'sort': None,
                  }
    for key, value in kwargs.items():
        if kwargs[key] is not "":
            query_dict[key] = value
    print(query_dict)

    def find_employers(**query_dict):
        q = Q()
        if query_dict['city']:
            q &= Q(city=query_dict['city'])
        if query_dict['query']:
            q2 = Q()
            q2 |= Q(title__icontains=query_dict['query'])  # search in title
            q2 |= Q(company__company_name__icontains=query_dict['query'])  # search in company name
            q2 |= Q(description__icontains=query_dict['query'])  # search in job description
            q &= q2
        if query_dict['selected1']:
            if query_dict['selected1'] == '1':  # filter by last 24 hours
                date_from = timezone.now() - timezone.timedelta(days=1)
                q &= Q(create_at__date__gte=date_from)
            if query_dict['selected1'] == '2':  # filter by last 1 week
                date_from = timezone.now() - timezone.timedelta(days=7)
                q &= Q(create_at__date__gte=date_from)
            if query_dict['selected1'] == '3':  # filter by last 1 mounth
                date_from = timezone.now() - timezone.timedelta(days=30)
                q &= Q(create_at__date__gte=date_from)

        if query_dict['selected2']:  # filter by education level
            q &= Q(education_level=query_dict['selected2'])

        if query_dict['selected3']:  # filter by experience level
            q &= Q(experience=query_dict['selected3'])

        if query_dict['selected4']:  # filter by gender
            q &= Q(gender=query_dict['selected4'])

        if query_dict['sort'] == 'descending':
            return UserProfile.objects.filter(q).order_by('-create_at')[:20]
        if query_dict['sort'] == 'ascending':
            return UserProfile.objects.filter(q).order_by('create_at')[:20]

        return UserProfile.objects.filter(q).order_by('-create_at')[:20]

    employers = UserProfile.objects.all()
    # employers = find_employers(**query_dict)

    if request.method == 'POST':
        form = EmployersSearchForm(request.POST)
        if form.is_valid():
            query_dict['query'] = form.cleaned_data['query']
            query_dict['city'] = form.cleaned_data['city']
            query_dict['category'] = form.cleaned_data['category']
            query_dict['selected1'] = form.cleaned_data['customRadio1']
            query_dict['selected2'] = form.cleaned_data['customRadio2']
            query_dict['selected3'] = form.cleaned_data['customRadio3']
            query_dict['selected4'] = form.cleaned_data['customRadio4']
            query_dict['sort'] = form.cleaned_data['sort']
            request.method = 'GET'
            return employersList(request, **query_dict)

    context = {'setting': setting,
               'employers': employers,
               'CITY': CITY,
               'query_dict': query_dict,
               }
    return render(request, 'employers-list.html', context)
