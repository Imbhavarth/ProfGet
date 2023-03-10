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
    path('dashboard/', views.dashboard, name='dashboard'),
    path('user_loged/', views.user_loged, name='user_loged'),
]