from django.http import HttpResponse
from django.shortcuts import render


def home(request):
    return render(request, 'index.html')
def login(request):
    if request.method == 'POST':
        username = request.POST['uname']
        password = request.POST['psw']
    return render(request,'authentification/login.html')

