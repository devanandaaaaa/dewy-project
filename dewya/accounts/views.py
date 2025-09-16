from django.shortcuts import render, redirect
from .forms import RegisterForm
from django.contrib import messages
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Account created. Welcome to The Dewy Ritual!")
            return redirect('store:product_list')
    else:
        form = RegisterForm()
    return render(request, 'accounts/register.html', {'form': form})

@login_required
def profile_page(request):
    return render(request, 'accounts/profile.html')

@login_required
def update_profile(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')

        user = request.user
        user.username = username
        user.email = email
        user.save()

        return redirect('accounts:profile')

    return redirect('accounts:profile')

