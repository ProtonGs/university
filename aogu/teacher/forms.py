from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Teacher

class TeacherRegistrationForm(UserCreationForm):
    iin = forms.CharField(max_length=12)
    identity_document = forms.CharField(max_length=255)
    registered_address = forms.CharField(max_length=255)
    residence_address = forms.CharField(max_length=255)
    phone_number = forms.CharField(max_length=20)
    email = forms.EmailField(max_length=255)
    publication_type = forms.CharField(max_length=50)
    publication_name = forms.CharField(max_length=255)
    publication_edition_name = forms.CharField(max_length=255)
    publication_edition_year = forms.IntegerField()
    publication_edition_number = forms.IntegerField()
    coauthors = forms.CharField(max_length=255)
    supporting_documents = forms.CharField(max_length=255)
    award_type = forms.CharField(max_length=50)
    honorary_title = forms.CharField(max_length=50)
    award_date = forms.CharField(max_length=255)
    qualification_improvement_form = forms.CharField(max_length=50)
    qualification_improvement_city = forms.CharField(max_length=255)
    qualification_improvement_organization_name = forms.CharField(max_length=255)
    qualification_improvement_start_date = forms.CharField(max_length=255)
    qualification_improvement_end_date = forms.CharField(max_length=255)
    qualification_improvement_duration = forms.CharField(max_length=255)
    qualification_improvement_topic = forms.CharField(max_length=255)
    qualification_improvement_supporting_document = forms.CharField(max_length=255)

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2', 'iin', 'identity_document', 'registered_address', 
                  'residence_address', 'phone_number', 'email', 'publication_type', 'publication_name',
                  'publication_edition_name', 'publication_edition_year', 'publication_edition_number', 'coauthors',
                  'supporting_documents', 'award_type', 'honorary_title', 'award_date', 'qualification_improvement_form',
                  'qualification_improvement_city', 'qualification_improvement_organization_name',
                  'qualification_improvement_start_date', 'qualification_improvement_end_date', 
                  'qualification_improvement_duration', 'qualification_improvement_topic', 
                  'qualification_improvement_supporting_document')

class TeacherUpdateForm(forms.ModelForm):
    class Meta:
        model = Teacher
        fields = ('iin', 'identity_document', 'registered_address', 'residence_address', 'phone_number', 'email',
                  'publication_type', 'publication_name', 'publication_edition_name', 'publication_edition_year', 
                  'publication_edition_number', 'coauthors', 'supporting_documents', 'award_type', 'honorary_title', 
                  'award_date', 'qualification_improvement_form', 'qualification_improvement_city', 
                  'qualification_improvement_organization_name', 'qualification_improvement_start_date', 
                  'qualification_improvement_end_date', 'qualification_improvement_duration', 
                  'qualification_improvement_topic', 'qualification_improvement_supporting_document')