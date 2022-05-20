from django.contrib import messages
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.models import User
from django.db.models import Count, Q
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.utils import timezone
from apply.models import Apply
from company.forms import ImageForm
from company.models import Company, CompanyPhotoGallery
from home import forms
from home.forms import CreateResumeForm, CompanyInfoForm, PostJobForm, SearchForm, ContactForm, FilterForm, SortForm
from home.models import ContactMessage, Setting, FAQ
from home.other import CITY, CATEGORY, EDUCATION_LEVEL, EXPERIENCE, GENDER_, JOB_TYPE
from job.models import Job
from user.models import UserProfile, UserEducation, UserExperience, UserSkills
from django.forms import modelformset_factory,formset_factory


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
    if request.method == 'POST':  # check post
        form = SearchForm(request.POST)
        if form.is_valid():
            q = Q()
            query = form.cleaned_data['query']
            if query != "":
                q |= Q(title__icontains=query)  # search from title
                q |= Q(company__company_name__icontains=query)  # search from company name
                q |= Q(description__icontains=query)  # search from description
            city = form.cleaned_data['city']
            if city != "":
                q &= Q(city=city)  # and search from city
            category = form.cleaned_data['category']
            if category != "":
                q &= Q(category=category)  # and search from category
            job_list = Job.objects.filter(q)[:20]

            context = {'setting': setting,
                       'job_list': job_list,
                       'CITY': CITY,
                       }
            return render(request, 'job-list.html', context)

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
            # messages.success(request, "Your message has ben sent. Thank you for your message.")
            return HttpResponseRedirect('/contactus')

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
    print(applied_this_job)
    if request.method == 'POST':  # check post
        data = Apply()  # create relation with model
        data.user_id = current_user.id
        data.job_id = job.id
        data.save()  # save data to table

        messages.success(request, "İlana başvuru yapıldı")
        return HttpResponseRedirect('/')
    context = {'setting': setting,
               'job': job,
               'applied_this_job':applied_this_job
               }
    return render(request, 'job-details.html', context)


@login_required(login_url='/login')  # Check login
@permission_required('user.add_userprofile', login_url='/login')
def createResume(request):
    setting = Setting.objects.get(id=1)
    current_user = request.user
    userprofile = UserProfile.objects.get(user_id=current_user.id)
    user_education = UserEducation.objects.filter(user_id=current_user.id)
    user_experience = UserEducation.objects.filter(user_id=current_user.id)

    if request.method == 'POST':  # check post
        form = CreateResumeForm(request.POST, request.FILES, )
        ItemFormSet = formset_factory(CreateResumeForm)
        item_formset = ItemFormSet()
        if form.is_valid():

            data = userprofile  # create relation with model
            data2 = UserEducation()
            data3 = UserExperience()
            data4 = UserSkills()
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

            education_count = int(form.cleaned_data['educationCount'])

            for item in item_formset:
                print(item)
                #print(item.cleaned_data.get('school'))

            for i in range(education_count):
                data2.user = current_user
                data2.school = form.cleaned_data['school']
                print(i)
                print(form.cleaned_data['school'])
                data2.degree = form.cleaned_data['degree']
                data2.department = form.cleaned_data['department']
                data2.start_date = form.cleaned_data['start_date']
                data2.end_date = form.cleaned_data['end_date']
                data2.education_add_info = form.cleaned_data['education_add_info']
                data2.save()

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

            data.save()  # save data to table
            data2.save()
            data3.save()
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


def candidatesProfile(request):
    setting = Setting.objects.get(id=1)
    current_user = request.user
    userprofile = UserProfile.objects.get(user_id=current_user.id)
    user_education = UserEducation.objects.all().filter(user_id=current_user.id)
    user_experience = UserExperience.objects.all().filter(user_id=current_user.id)
    user_skills = UserSkills.objects.all().filter(user_id=current_user.id)
    applied = Apply.objects.values_list('job_id').filter(user_id=current_user.id)
    applied_jobs = Job.objects.filter(id__in=applied)
    jobs_for_me = Job.objects.all()  # düzelt

    context = {'setting': setting,
               'userprofile': userprofile,
               'user_education': user_education,
               'user_experience': user_experience,
               'user_skills': user_skills,
               'applied_jobs': applied_jobs,
               'jobs_for_me': jobs_for_me
               }
    return render(request, 'candidates-profile.html', context)


@login_required(login_url='/login')  # Check login
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
    current_user = request.user
    company = Company.objects.get(slug=slug)
    gallery = CompanyPhotoGallery.objects.filter(company_id=company.id)

    company_job = Job.objects.filter(company_id=company.id)
    ImageFormSet = modelformset_factory(CompanyPhotoGallery, form=ImageForm, extra=5)
    formset = ImageFormSet(queryset=CompanyPhotoGallery.objects.none())

    if request.method == "POST":
        formset = ImageFormSet(request.POST, request.FILES)
        if formset.is_valid():
            for f in formset.cleaned_data:
                if f:
                    image = f['image']
                    CompanyPhotoGallery.objects.create(image=image, company=company)
            context = {'setting': setting,
                       'company': company,
                       'company_job': company_job,
                       'gallery': gallery,
                       "formset": formset
                       }
            return render(request, 'company-detail.html', context)
        else:
            print(formset.errors)

    context = {'setting': setting,
               'company': company,
               'company_job': company_job,
               'gallery': gallery,
               "formset": formset
               }
    return render(request, 'company-detail.html', context)


def jobList(request):
    setting = Setting.objects.get(id=1)
    job_list = Job.objects.all().order_by('-create_at')[:20]
    all_categories = Job.objects.values_list('category', flat=True).distinct()
    q = Q()
    if request.method == 'POST':
        if request.method == 'POST' and 'search-form' in request.POST:
            form = SearchForm(request.POST)
            if form.is_valid():
                query = form.cleaned_data['query']
                if query != "":
                    q |= Q(title__icontains=query)
                    q |= Q(company__company_name__icontains=query)
                    q |= Q(description__icontains=query)
                city = form.cleaned_data['city']
                if city != "":  # and search from city
                    q &= Q(city=city)
                category = form.cleaned_data['category']
                if category != "":
                    q &= Q(category=category)

        if request.method == 'POST' and 'filter-form' in request.POST:
            form = FilterForm(request.POST)
            if form.is_valid():
                selected1 = form.cleaned_data['customRadio1']
                selected2 = form.cleaned_data['customRadio2']
                selected3 = form.cleaned_data['customRadio3']
                selected4 = form.cleaned_data['customRadio4']

                if selected1 == '1':  # filter by last 24 hours
                    date_from = timezone.now() - timezone.timedelta(days=1)
                    q &= Q(create_at__date__gte=date_from)
                if selected1 == '2':  # filter by last 1 week
                    date_from = timezone.now() - timezone.timedelta(days=7)
                    q &= Q(create_at__date__gte=date_from)
                if selected1 == '3':  # filter by last 1 mounth
                    date_from = timezone.now() - timezone.timedelta(days=30)
                    q &= Q(create_at__date__gte=date_from)

                if selected2 != '':  # filter by education level
                    q &= Q(education_level=selected2)

                if selected3 != '':  # filter by experience level
                    q &= Q(experience=selected3)

                if selected4 != '':  # filter by gender
                    q &= Q(gender=selected4)
        job_list = Job.objects.filter(q).order_by('-create_at')[:20]

        if request.method == 'POST' and 'sort' in request.POST:
            print("burada")
            form = SortForm(request.POST)
            if form.is_valid():
                sort = form.cleaned_data['sort']

                print(sort)
                if sort == 'descending':
                    job_list = Job.objects.filter(q).order_by('-create_at')[:20]
                if sort == 'ascending':
                    job_list = Job.objects.filter(q).order_by('create_at')[:20]

        context = {'setting': setting,
                   'job_list': job_list,
                   'CITY': CITY,
                   'all_categories': all_categories,
                   }
        return render(request, 'job-list.html', context)

    context = {'setting': setting,
               'job_list': job_list,
               'CITY': CITY,
               'all_categories': all_categories,
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
               'CATEGORY': CATEGORY,
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


def employersList(request):
    setting = Setting.objects.get(id=1)
    # employers = User.objects.filter(groups=2)  # job_seeker
    employers = UserProfile.objects.all()
    print(employers)
    context = {'setting': setting,
               'CITY': CITY,
               'employers': employers
               }
    return render(request, 'employers-list.html', context)
