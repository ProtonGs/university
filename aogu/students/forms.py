from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Student


class StudentRegistrationForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=True, help_text='Required.')
    last_name = forms.CharField(max_length=30, required=True, help_text='Required.')
    email = forms.EmailField(max_length=254, required=True, help_text='Required. Enter a valid email address.')
    iin = forms.CharField(max_length=12, required=True, help_text='Required. Enter a valid IIN.')
    identity_document = forms.CharField(max_length=255, required=True, help_text='Required.')
    marital_status = forms.CharField(max_length=50, required=True, help_text='Required.')
    study_type = forms.CharField(max_length=50, required=True, help_text='Required.')
    registered_address = forms.CharField(max_length=255, required=True, help_text='Required.')
    residence_address = forms.CharField(max_length=255, required=True, help_text='Required.')
    phone_number = forms.CharField(max_length=20, required=True, help_text='Required. Enter a valid contact number.')
    course_number = forms.IntegerField(required=True, help_text='Required.')
    parents = forms.CharField(max_length=255, required=True, help_text='Required.')
    parents_contacts = forms.CharField(max_length=255, required=True, help_text='Required.')
    parents_work_place = forms.CharField(max_length=255, required=True, help_text='Required.')
    certificates_or_olympiads = forms.CharField(max_length=255, required=True, help_text='Required.')
    disability = forms.BooleanField(required=False)
    hobbies = forms.CharField(max_length=255, required=True, help_text='Required.')
    religious_beliefs = forms.CharField(max_length=255, required=True, help_text='Required.')

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']

    def save(self, commit=True):
        user = super().save(commit=False)
        user.is_student = True
        user.save()
        student = Student.objects.create(
            user=user,
            iin=self.cleaned_data['iin'],
            identity_document=self.cleaned_data['identity_document'],
            marital_status=self.cleaned_data['marital_status'],
            study_type=self.cleaned_data['study_type'],
            registered_address=self.cleaned_data['registered_address'],
            residence_address=self.cleaned_data['residence_address'],
            phone_number=self.cleaned_data['phone_number'],
            email=self.cleaned_data['email'],
            course_number=self.cleaned_data['course_number'],
            parents=self.cleaned_data['parents'],
            parents_contacts=self.cleaned_data['parents_contacts'],
            parents_work_place=self.cleaned_data['parents_work_place'],
            certificates_or_olympiads=self.cleaned_data['certificates_or_olympiads'],
            disability=self.cleaned_data['disability'],
            hobbies=self.cleaned_data['hobbies'],
            religious_beliefs=self.cleaned_data['religious_beliefs']
        )
        return user, student