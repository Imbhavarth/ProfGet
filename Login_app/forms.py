from django import forms
from django.contrib.auth.models import User
from Login_app.models import UserInfo,JobProviderInfo,Invite


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    class Meta():
        model = User
        fields = ('username','email','password')

class UserInfoForm(forms.ModelForm):
    dob = forms.DateField(widget=forms.TextInput(attrs={'type':'date',}))
    class Meta():
        model = UserInfo
        fields = ('firstname','lastname','dob','country','skills','qualification','experience','gender','linked_id','resume','profile_pic')

class JobProviderInfoForm(forms.ModelForm):
    class Meta():
        model = JobProviderInfo
        fields = ('company_name',)

class EditProfile(forms.ModelForm):
    dob = forms.DateField(widget=forms.TextInput(attrs={'type':'date',}))
    class Meta:
        model = UserInfo
        exclude = ('user',)


class InviteForm(forms.ModelForm):
    class Meta:
        model = Invite
        fields = ('friend_email',)
