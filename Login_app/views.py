from django.shortcuts import render
from Login_app.forms import UserForm,UserInfoForm,JobProviderInfoForm,EditProfile,InviteForm
from Login_app.models import UserInfo,User
from Post_app.forms import PostForm, ChatForm
from Post_app.models import Post, Chat
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.http import  HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.core.mail import send_mail
from django.conf import settings
from email.message import EmailMessage
import ssl
import smtplib

email_sender = 'profget6@gmail.com'
email_password = settings.EMAIL_PASS


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
                return HttpResponseRedirect(reverse('Login_app:dashboard_seeker'))
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
def dashboard_seeker(request):
    posts = Post.objects.filter()
    if UserInfo.objects.get(user=request.user):
        current_user = UserInfo.objects.get(user=request.user)
    user_skill = current_user.skills
    user_skill_list = user_skill.split(',')
    for skill in user_skill_list:
        print(skill)
        matching_skills = Post.objects.filter(project_requirement__icontains = skill)

    if request.method == 'GET':
        search = request.GET.get('search','')
        result = Post.objects.filter(project_name__icontains=search)

    return render(request,'authentification/dashboard_seeker.html', context={'posts':posts, 'search':search, 'result':result, 'matching_skills':matching_skills})

@login_required
def dashboard_seeker1(request):
    posts = Post.objects.filter()

    if request.method == 'GET':
        search = request.GET.get('search','')
        result = Post.objects.filter(project_name__icontains=search)

    return render(request,'authentification/dashboard_seeker.html', context={'posts':posts, 'search':search, 'result':result})

@login_required
def dashboard_provider(request):
    return render(request,'authentification/dashboard_provider.html')

@login_required
def profile_seeker(request):
    return render(request,'profile_seeker.html')

@login_required
def profile_provider(request):
    return render(request,'profile_provider.html')

@login_required
def chatbot(request):
    return render(request,'chatbot.html')

@login_required
def post_project(request):
        form = PostForm()
        if request.method == 'POST':
            form = PostForm(request.POST)
            if form.is_valid():
                post = form.save(commit=False)
                post.author = request.user
                post.save()
                return HttpResponseRedirect(reverse('Login_app:dashboard_provider'))
        return render(request,'post_project.html', context={'title':'Post Project','form':form})

@login_required
def chat(request):
        chats = Chat.objects.filter()
        form = ChatForm()
        if request.method == 'POST':
            form = ChatForm(request.POST)
            if form.is_valid():
                sms = form.save(commit=False)
                sms.author = request.user
                sms.save()
                return HttpResponseRedirect(reverse('Login_app:chat'))
        return render(request,'chat.html', context={'title':'Chat Room','form':form, 'chats':chats})

@login_required
def invite(request):
    form = InviteForm()
    if request.method == 'POST':
        current_user = UserInfo.objects.get(user=request.user)
        name = current_user.firstname
        email = request.POST.get('friend_email')
        email_receiver = email
        subject = "Invitation to join PROFGET by Yellow Fafda."
        body = f"""
Hi, I am {name}, using Profget for freelancing to get projects. This is the most efficient website for freelancing.
Link:http://127.0.0.1:8000/

Thank You
"""

        em = EmailMessage()
        em['From'] = email_sender
        em['To'] = email_receiver
        em['subject'] = subject
        em.set_content(body)

        context = ssl.create_default_context()

        with smtplib.SMTP_SSL('smtp.gmail.com',465,context=context) as smtp:
            smtp.login(email_sender, email_password)
            smtp.sendmail(email_sender, email_receiver, em.as_string())
        return HttpResponseRedirect(reverse('Login_app:dashboard_seeker'))
    return render(request,'invite.html', context={'title':'Invitation','form':form})
        


@login_required
def edit_profile(request):
    current_user = UserInfo.objects.get(user=request.user)
    form = EditProfile(instance=current_user)

    if request.method == 'POST':
        form = EditProfile(request.POST, request.FILES, instance=current_user)
        if form.is_valid():
            form.save(commit=True)
            form = EditProfile(instance=current_user)
            return HttpResponseRedirect(reverse('Login_app:profile_seeker'))
    return render(request, 'edit_profile.html', context={'form':form})
        
        

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
            return HttpResponseRedirect(reverse('Login_app:login'))
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
            job_provider_info.save()

            jpregistered = True
            return HttpResponseRedirect(reverse('Login_app:login'))
    else:
        user_form = UserForm()
        job_provider_info_form = JobProviderInfoForm()


    dict = {'user_form':user_form, 'job_provider_info_form':job_provider_info_form}
    return render(request, 'authentification/jobproviderregister.html', context=dict)

@login_required 
def feedback(request):
    users = User.objects.filter()

    if request.method == 'GET':
        search = request.GET.get('search','')
        results = User.objects.filter(username__icontains=search)
    return render(request, 'feedback_page.html', context={'users':users, 'search':search, 'results':results})