from django import forms
from django.contrib.auth.models import User
from Login_app.models import UserInfo,JobProviderInfo


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    class Meta():
        model = User
        fields = ('username','email','password')

class UserInfoForm(forms.ModelForm):
   
    class Meta():
        model = UserInfo
        fields = ('firstname','lastname','linked_id','country','skills','qualification','experience','gender')

class JobProviderInfoForm(forms.ModelForm):
    class Meta():
        model = JobProviderInfo
        fields = ('company_name','project_description')

