from django import forms
from django.contrib.auth.models import User
from Post_app.models import Post

class PostForm(forms.ModelForm):

    class Meta():
        model = Post
        fields = ['project_name','project_description','project_requirement','project_rate']