from django.shortcuts import render
from Login_app.forms import UserForm,UserInfoForm,JobProviderInfoForm

from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.http import  HttpResponse, HttpResponseRedirect
from django.urls import reverse

# Create your views here.

def index(request):
    dict = {}
    return render(request, 'index.html', context=dict)

def login_page(request):
    return render(request,'authentification/login.html')

def option(request):
    return render(request,'authentification/option.html')

def user_loged(request):
    if  request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect(reverse('Login_app:dashboard'))
            else:
                return HttpResponse("Account is not active.")
        else:
            return HttpResponse("Wrong Login details.")
    else:
        return HttpResponseRedirect(reverse('Login_app:login'))

@login_required    
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('Login_app:login'))

@login_required
def dashboard(request):
    return render(request,'authentification/dashboard.html')
        
        

def register(request):

    registered = False

    if request.method == 'POST':
        user_form = UserForm(data=request.POST)
        user_info_form = UserInfoForm(data=request.POST)

        if user_form.is_valid() and user_info_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()

            user_info = user_info_form.save(commit=False)
            user_info.user =user

            if 'profile_pic' in request.FILES:
                user_info.profile_pic = request.FILES['profile_pic']

            user_info.save()

            registered = True
    else:
        user_form = UserForm()
        user_info_form = UserInfoForm()


    dict = {'user_form':user_form, 'user_info_form':user_info_form}
    return render(request, 'authentification/register.html', context=dict)

def jobproviderregister(request):

    jpregistered = False

    if request.method == 'POST':
        user_form = UserForm(data=request.POST)
        job_provider_info_form = JobProviderInfoForm(data=request.POST)

        if user_form.is_valid() and job_provider_info_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()

            job_provider_info = job_provider_info_form.save(commit=False)
            job_provider_info.user =user

            # if 'project_file' in request.FILES:
            #     job_provider_info.project_file = request.FILES['project_file']

            job_provider_info.save()

            jpregistered = True
    else:
        user_form = UserForm()
        job_provider_info_form = JobProviderInfoForm()


    dict = {'user_form':user_form, 'job_provider_info_form':job_provider_info_form}
    return render(request, 'authentification/jobproviderregister.html', context=dict)