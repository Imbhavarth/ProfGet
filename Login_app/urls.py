from django.urls import path
from Login_app import views

app_name = 'Login_app'

urlpatterns = [
    path('', views.index, name='index'),
    path('register/', views.register, name='register'),
    path('jobproviderregister/', views.jobproviderregister, name='jobproviderregister'),
    path('login/', views.login_page, name='login'),
    path('option/', views.option, name='option'),
    path('logout/', views.user_logout, name='logout'),
    path('dashboard_seeker/', views.dashboard_seeker, name='dashboard_seeker'),
    path('dashboard_provider/', views.dashboard_provider, name='dashboard_provider'),
    path('user_loged/', views.user_loged, name='user_loged'),
    path('profile_seeker/', views.profile_seeker, name='profile_seeker'),
    path('profile_provider/', views.profile_provider, name='profile_provider'),
    path('edit_profile/', views.edit_profile, name='edit_profile'),
    path('post_project/', views.post_project, name='post_project'),
    path('invite/', views.invite, name='invite'),
    path('feedback/', views.feedback, name='feedback'),
    path('chatbot/', views.chatbot, name='chatbot'),

    
]