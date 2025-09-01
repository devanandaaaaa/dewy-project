from django.shortcuts import render, redirect
from .forms import RegisterForm
from django.contrib import messages
from django.contrib.auth import login

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



