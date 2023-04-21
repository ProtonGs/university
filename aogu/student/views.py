
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from .forms import StudentRegistrationForm
from .models import Student

def register_student(request):
    if request.method == 'POST':
        form = StudentRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.save() # save the user object
            student = form.save(commit=False)
            student.user = user
            student.save()
            user = form.save(commit=False)
            student = Student(user=user)
            student.iin = form.cleaned_data['iin']
            student.identity_document = form.cleaned_data['identity_document']
            student.marital_status = form.cleaned_data['marital_status']
            student.study_type = form.cleaned_data['study_type']
            student.registered_address = form.cleaned_data['registered_address']
            student.residence_address = form.cleaned_data['residence_address']
            student.phone_number = form.cleaned_data['phone_number']
            student.email = form.cleaned_data['email']
            student.course_number = form.cleaned_data['course_number']
            student.parents = form.cleaned_data['parents']
            student.parents_contacts = form.cleaned_data['parents_contacts']
            student.parents_work_place = form.cleaned_data['parents_work_place']
            student.certificates_or_olympiads = form.cleaned_data['certificates_or_olympiads']
            student.disability = form.cleaned_data['disability']
            student.hobbies = form.cleaned_data['hobbies']
            student.religious_beliefs = form.cleaned_data['religious_beliefs']
            student.save()
            login(request, user)
            return redirect('home')
    else:
        form = StudentRegistrationForm()
    return render(request, 'student/register_student.html', {'form': form})