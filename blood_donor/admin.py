from django.contrib import admin
from django.contrib.auth.models import Group
from . models import BloodDonor

# Register your models here.

admin.site.register(BloodDonor)

admin.site.unregister(Group)