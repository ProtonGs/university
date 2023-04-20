from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from .forms import StudentRegistrationForm

def register_student(request):
    if request.method == 'POST':
        form = StudentRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('home')
    else:
        form = StudentRegistrationForm()
        return render(request, 'students/register_student.html', {'form': form})