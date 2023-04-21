from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Student

class StudentRegistrationForm(UserCreationForm):
    iin = forms.CharField(max_length=12)
    identity_document = forms.CharField(max_length=255)
    marital_status = forms.CharField(max_length=50)
    study_type = forms.CharField(max_length=50)
    registered_address = forms.CharField(max_length=255)
    residence_address = forms.CharField(max_length=255)
    phone_number = forms.CharField(max_length=20)
    email = forms.EmailField(max_length=255)
    course_number = forms.IntegerField()
    parents = forms.CharField(max_length=255)
    parents_contacts = forms.CharField(max_length=255)
    parents_work_place = forms.CharField(max_length=255)
    certificates_or_olympiads = forms.CharField(max_length=255)
    disability = forms.BooleanField(required=False)
    hobbies = forms.CharField(max_length=255)
    religious_beliefs = forms.CharField(max_length=255)

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2', 'iin', 'identity_document', 'marital_status', 'study_type', 
                  'registered_address', 'residence_address', 'phone_number', 'course_number', 'parents', 'parents_contacts',
                  'parents_work_place', 'certificates_or_olympiads', 'disability', 'hobbies', 'religious_beliefs')


class StudentUpdateForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ('iin', 'identity_document', 'marital_status', 'study_type', 'registered_address', 'residence_address',
                  'phone_number', 'email', 'course_number', 'parents', 'parents_contacts', 'parents_work_place',
                  'certificates_or_olympiads', 'disability', 'hobbies', 'religious_beliefs')
