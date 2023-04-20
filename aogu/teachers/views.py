from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from .forms import TeacherRegistrationForm

def register_teacher(request):
    if request.method == 'POST':
        form = TeacherRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('home')
    else:
        form = TeacherRegistrationForm()
        return render(request, 'teachers/register_teacher.html', {'form': form})