# Generated by Django 4.1.7 on 2023-03-27 23:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Login_app', '0012_alter_userinfo_profile_pic'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userinfo',
            name='country',
            field=models.CharField(choices=[('AU', 'Australia'), ('CA', 'Canada'), ('CH', 'China'), ('CO', 'Colombia'), ('FR', 'France'), ('IN', 'India'), ('NZ', 'New Zealand'), ('JP', 'Japan'), ('UK', 'United Kingdom'), ('US', 'United States')], max_length=22, null=True),
        ),
    ]
