from django.db import models

# Create your models here.
from django.contrib.admin import AdminSite

class MyAdminSite(AdminSite):
    site_header = ''

admin_site = MyAdminSite()