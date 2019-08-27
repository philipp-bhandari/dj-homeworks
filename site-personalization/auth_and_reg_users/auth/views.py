from django.shortcuts import render, redirect
from django.urls import reverse

from .forms import UserSignupForm


def home(request):
    username = 'гость'
    is_logged = request.user.is_authenticated

    if is_logged:
        username = request.user

    context = {
        'is_logged': is_logged,
        'username': username
    }

    return render(
        request,
        'home.html',
        context
    )


def signup(request):
    if request.method == 'POST':
        register_form = UserSignupForm(request.POST)

        if register_form.is_valid():
            register_form.save()
            return redirect(reverse('login'))
    else:
        register_form = UserSignupForm()

    context = {'form': register_form}

    return render(request, 'registration/signup.html', context)
