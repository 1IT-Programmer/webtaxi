from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Trip
from .forms import SignUpForm

def home(request):
    """Главная страница для всех пользователей"""
    return render(request, 'core/home.html')

@login_required
def create_trip(request):
    """Создание новой поездки (для пассажиров)"""
    if request.method == 'POST':
        # Логика обработки формы
        return redirect('home')
    return render(request, 'core/create_trip.html')
