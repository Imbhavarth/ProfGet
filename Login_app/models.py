from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class UserInfo(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='user_info')

    firstname =  models.CharField(max_length=22,null=True)

    lastname =  models.CharField(max_length=22,null=True)

    gender = (
            ('Male','Male'),
            ('Female','Female'),
             ('Do not want to disclose','Do not want to disclose'),
            )
    
    gender =  models.CharField(max_length=24,choices= gender, null=True)

    dob = models.DateField(blank=True, null=True)

    country = (
        ('AU','Australia'),
        ('CA','Canada'),
        ('CH','China'),
        ('CO','Colombia'),
        ('FR','France'),
        ('IN','India'),
        ('NZ','New Zealand'),
        ('JP','Japan'),
        ('UK','United Kingdom'),
        ('US','United States'),
    )                          
    country =  models.CharField(max_length=22,choices= country, null=True)

    skills = models.CharField(max_length=50, null=True)

    qualification = models.CharField(max_length=50, null=True)

    experience = models.CharField(max_length=50, null=True)

    linked_id = models.CharField(max_length=22,null=True)

    resume = models.FileField(upload_to="resume", blank=True)
    
    profile_pic = models.ImageField(upload_to='profile_pic', blank=True)


    def __str__(self):
        return self.user.username
    
class JobProviderInfo(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='job_provider_info')

    company_name = models.CharField(max_length=50, null=True)

    project_description = models.CharField(max_length=50, null=True)

    project_file = models.FileField(upload_to='project_file', blank=True)

    def __str__(self):
        return self.user.username
    
class Invite(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='invite')
    friend_email = models.EmailField(max_length=50, null=True)
    
    def __str__(self):
        return self.user.username


    

