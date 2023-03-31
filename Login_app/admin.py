from django.contrib import admin
from Login_app.models import UserInfo,JobProviderInfo,Invite

# Register your models here.

admin.site.register(UserInfo)
admin.site.register(JobProviderInfo)
admin.site.register(Invite)