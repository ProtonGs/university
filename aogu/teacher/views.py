from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from .forms import TeacherRegistrationForm
from .models import Teacher

def register_teacher(request):
    if request.method == 'POST':
        form = TeacherRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.save() # save the user object
            teacher = form.save(commit=False)
            teacher.user = user
            teacher.save()
            user = form.save(commit=False)
            teacher = Teacher(user=user)
            teacher.iin = form.cleaned_data['iin']
            teacher.identity_document = form.cleaned_data['identity_document']
            teacher.registered_address = form.cleaned_data['registered_address']
            teacher.residence_address = form.cleaned_data['residence_address']
            teacher.phone_number = form.cleaned_data['phone_number']
            teacher.email = form.cleaned_data['email']
            teacher.publication_type = form.cleaned_data['publication_type']
            teacher.publication_name = form.cleaned_data['publication_name']
            teacher.publication_edition_name = form.cleaned_data['publication_edition_name']
            teacher.publication_edition_year = form.cleaned_data['publication_edition_year']
            teacher.publication_edition_number = form.cleaned_data['publication_edition_number']
            teacher.coauthors = form.cleaned_data['coauthors']
            teacher.supporting_documents = form.cleaned_data['supporting_documents']
            teacher.award_type = form.cleaned_data['award_type']
            teacher.honorary_title = form.cleaned_data['honorary_title']
            teacher.award_date = form.cleaned_data['award_date']
            teacher.qualification_improvement_form = form.cleaned_data['qualification_improvement_form']
            teacher.qualification_improvement_city = form.cleaned_data['qualification_improvement_city']
            teacher.qualification_improvement_organization_name = form.cleaned_data['qualification_improvement_organization_name']
            teacher.qualification_improvement_start_date = form.cleaned_data['qualification_improvement_start_date']
            teacher.qualification_improvement_end_date = form.cleaned_data['qualification_improvement_end_date']
            teacher.qualification_improvement_duration = form.cleaned_data['qualification_improvement_duration']
            teacher.qualification_improvement_topic = form.cleaned_data['qualification_improvement_topic']
            teacher.qualification_improvement_supporting_document = form.cleaned_data['qualification_improvement_supporting_document']
            teacher.save()
            login(request, user)
            return redirect('home')
    else:
        form = TeacherRegistrationForm()
    return render(request, 'teacher/register_teacher.html', {'form': form})