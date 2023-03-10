from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class UserInfo(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    firstname =  models.CharField(max_length=22,null=True)

    lastname =  models.CharField(max_length=22,null=True)

    linked_id = models.CharField(max_length=22,null=True)

    # resume = models.FileField(upload_to="media/resume", null=True)

    gender = (
            ('Male','Male'),
            ('Female','Female'),
             ('Do not want to disclose','Do not want to disclose'),
            )
    
    gender =  models.CharField(max_length=24,choices= gender, null=True)

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
    country =  models.CharField(max_length=22,choices= country)

    skills = models.CharField(max_length=50, null=True)

    qualification = models.CharField(max_length=50, null=True)

    experience = models.CharField(max_length=50, null=True)


    def __str__(self):
        return self.user.username
    
class JobProviderInfo(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    company_name = models.CharField(max_length=50, null=True)

    project_description = models.CharField(max_length=50, null=True)

    # project_file = models.FileField(upload_to='media/project_file')

    def __str__(self):
        return self.user.username

    
