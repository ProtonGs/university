from django.db import models
from django.contrib.auth.models import User

# Create your models here.
from django.db import models

class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    iin = models.CharField(max_length=12)
    identity_document = models.CharField(max_length=255)
    marital_status = models.CharField(max_length=50)
    study_type = models.CharField(max_length=50)
    registered_address = models.CharField(max_length=255)
    residence_address = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=20)
    email = models.EmailField(max_length=255)
    course_number = models.PositiveIntegerField()
    parents = models.CharField(max_length=255)
    parents_contacts = models.CharField(max_length=255)
    parents_work_place = models.CharField(max_length=255)
    certificates_or_olympiads = models.CharField(max_length=255)
    disability = models.BooleanField(default=False)
    hobbies = models.CharField(max_length=255)
    religious_beliefs = models.CharField(max_length=255)
