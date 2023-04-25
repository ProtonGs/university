from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import ChangeLoginForm

def login(request):
    render(request, 'accounts/login.html',)



from django.contrib.auth import login
from .forms import UserRegistrationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import PasswordChangeView



def register(request):
    if request.user.is_authenticated:
        return redirect('home')

    if request.method == "POST":
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')

        else:
            for error in list(form.errors.values()):
                print(request, error)

    else:
        form = UserRegistrationForm()

    return render(
        request=request,
        template_name = "registration/register.html",
        context={"form": form}
    )



class PasswordChangeView(LoginRequiredMixin, PasswordChangeView):
    template_name = 'change_password.html'
    success_url = '/'


@login_required
def profile(request):
    user = request.user
    context = {'user': user}
    return render(request, 'registration/profile.html', context)




@login_required
def change_login(request):
    if request.method == 'POST':
        form = ChangeLoginForm(request.POST)
        if form.is_valid():
            current_login = form.cleaned_data['current_login']
            new_login = form.cleaned_data['new_login']
            user = request.user
            if user.check_password(form.cleaned_data['password']):
                if user.username == current_login:
                    user.username = new_login
                    user.save()
                    messages.success(request, 'Your login has been updated.')
                    return redirect('home')
                else:
                    messages.error(request, 'Invalid current login.')
            else:
                messages.error(request, 'Invalid password.')
    else:
        form = ChangeLoginForm()
    return render(request, 'registration/change_login.html', {'form': form})

