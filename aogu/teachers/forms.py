from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Teacher

class TeacherRegistrationForm(UserCreationForm):
    iin = forms.CharField(max_length=12, required=True, help_text='Required. Enter a valid IIN.')
    identity_document = forms.CharField(max_length=255, required=True, help_text='Required. Enter a valid identity document.')
    registered_address = forms.CharField(max_length=255, required=True, help_text='Required. Enter registered address.')
    residence_address = forms.CharField(max_length=255, required=True, help_text='Required. Enter residence address.')
    phone_number = forms.CharField(max_length=20, required=True, help_text='Required. Enter a valid contact number.')
    email = forms.EmailField(max_length=255, required=True, help_text='Required. Enter a valid email address.')
    publication_type = forms.CharField(max_length=50, required=False, help_text='Optional. Enter publication type.')
    publication_name = forms.CharField(max_length=255, required=False, help_text='Optional. Enter publication name.')
    publication_edition_name = forms.CharField(max_length=255, required=False, help_text='Optional. Enter publication edition name.')
    publication_edition_year = forms.IntegerField(required=False, help_text='Optional. Enter publication edition year.')
    publication_edition_number = forms.IntegerField(required=False, help_text='Optional. Enter publication edition number.')
    coauthors = forms.CharField(max_length=255, required=False, help_text='Optional. Enter coauthors.')
    supporting_documents = forms.CharField(max_length=255, required=False, help_text='Optional. Enter supporting documents.')
    award_type = forms.CharField(max_length=50, required=False, help_text='Optional. Enter award type.')
    honorary_title = forms.CharField(max_length=50, required=False, help_text='Optional. Enter honorary title.')
    award_date = forms.DateField(required=False, help_text='Optional. Enter award date.')
    qualification_improvement_form = forms.CharField(max_length=50, required=False, help_text='Optional. Enter qualification improvement form.')
    qualification_improvement_city = forms.CharField(max_length=255, required=False, help_text='Optional. Enter qualification improvement city.')
    qualification_improvement_organization_name = forms.CharField(max_length=255, required=False, help_text='Optional. Enter qualification improvement organization name.')
    qualification_improvement_start_date = forms.DateField(required=False, help_text='Optional. Enter qualification improvement start date.')
    qualification_improvement_end_date = forms.DateField(required=False, help_text='Optional. Enter qualification improvement end date.')
    qualification_improvement_duration = forms.IntegerField(required=False, help_text='Optional. Enter qualification improvement duration.')
    qualification_improvement_topic = forms.CharField(max_length=255, required=False, help_text='Optional. Enter qualification improvement topic.')
    qualification_improvement_supporting_document = forms.CharField(max_length=255, required=False, help_text='Optional. Enter qualification improvement supporting document.')

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')

    def save(self, commit=True):
        user = super().save(commit=False)
        user.is_teacher = True
        user.save()
        teacher = Teacher.objects.create(
            user=user,
            iin=self.cleaned_data['iin'],
            identity_document=self.cleaned_data['identity_document'],
            registered_address=self.cleaned_data['registered_address'],
            residence_address=self.cleaned_data['residence_address'],
            phone_number=self.cleaned_data['phone_number'],
            email=self.cleaned_data['email'],
            publication_type=self.cleaned_data['publication_type'],
            publication_name=self.cleaned_data['publication_name'],
            publication_edition_name=self.cleaned_data['publication_edition_name'],
            publication_edition_year=self.cleaned_data['publication_edition_year'],
            publication_edition_number=self.cleaned_data['publication_edition_number'],
            coauthors=self.cleaned_data['coauthors'],
            supporting_documents=self.cleaned_data['supporting_documents'],
            award_type=self.cleaned_data['award_type'],
            honorary_title=self.cleaned_data['honorary_title'],
            award_date=self.cleaned_data['award_date'],
            qualification_improvement_form=self.cleaned_data['qualification_improvement_form'],
            qualification_improvement_city=self.cleaned_data['qualification_improvement_city'],
            qualification_improvement_organization_name=self.cleaned_data['qualification_improvement_organization_name'],
            qualification_improvement_start_date=self.cleaned_data['qualification_improvement_start_date'],
            qualification_improvement_end_date=self.cleaned_data['qualification_improvement_end_date'],
            qualification_improvement_duration=self.cleaned_data['qualification_improvement_duration'],
            qualification_improvement_topic=self.cleaned_data['qualification_improvement_topic'],
            qualification_improvement_supporting_document=self.cleaned_data['qualification_improvement_supporting_document']
        )
        return user, teacher