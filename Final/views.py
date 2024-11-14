# Plantillas
from django.shortcuts import render
# Mensajes
from django.contrib import messages

# Vista home
def home(request):
    return render(request,'home.html')