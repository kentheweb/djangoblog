from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import RegisterUser
# Create your views here.


def register(request):
    if request.method == 'POST':
        form = RegisterUser(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, 'account created successfully for {0} you can now login to your account'.format(username))
            return redirect('login-route')
    else:
        form = RegisterUser()

    context = {
        'form' : form
    }
    return render(request, 'users/register.html', context)
@login_required
def profile(request):
    return render(request, 'users/profile.html')