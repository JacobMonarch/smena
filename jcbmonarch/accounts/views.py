# accounts/views.py

from django.shortcuts import render, redirect
from .forms import CustomUserCreationForm
from django.contrib import messages

def login_view(request):
    return render(request, 'accounts/login.html')

def register_view(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Регистрация прошла успешно! Теперь войдите в систему.")
            return redirect('login')  # редирект на страницу входа с сообщением
    else:
        form = CustomUserCreationForm()
    return render(request, 'accounts/register.html', {'form': form})
    