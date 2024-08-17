# app/views.py
# Aquí definimos las vistas que manejarán la lógica de negocio.
from django.shortcuts import render

def home(request):
    # Vista para la página de inicio
    return render(request, 'app/home.html')

def profile(request):
    # Vista para la página de perfil de usuario
    return render(request, 'app/profile.html')
