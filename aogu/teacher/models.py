from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Teacher(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    iin = models.CharField(max_length=12)
    identity_document = models.CharField(max_length=255)
    registered_address = models.CharField(max_length=255)
    residence_address = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=20)
    email = models.EmailField(max_length=255)
    publication_type = models.CharField(max_length=50)
    publication_name = models.CharField(max_length=255)
    publication_edition_name = models.CharField(max_length=255)
    publication_edition_year = models.PositiveIntegerField()
    publication_edition_number = models.PositiveIntegerField()
    coauthors = models.CharField(max_length=255)
    supporting_documents = models.CharField(max_length=255)
    award_type = models.CharField(max_length=50)
    honorary_title = models.CharField(max_length=50)
    award_date = models.CharField(max_length=255)
    qualification_improvement_form = models.CharField(max_length=50)
    qualification_improvement_city = models.CharField(max_length=255)
    qualification_improvement_organization_name = models.CharField(max_length=255)
    qualification_improvement_start_date = models.CharField(max_length=255)
    qualification_improvement_end_date = models.CharField(max_length=255)
    qualification_improvement_duration = models.CharField(max_length=255)
    qualification_improvement_topic = models.CharField(max_length=255)
    qualification_improvement_supporting_document = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.user} {self.user.last_name}"