# Generated by Django 4.1.7 on 2023-03-09 02:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Login_app', '0008_alter_userinfo_resume'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='jobproviderinfo',
            name='project_file',
        ),
        migrations.RemoveField(
            model_name='userinfo',
            name='resume',
        ),
    ]