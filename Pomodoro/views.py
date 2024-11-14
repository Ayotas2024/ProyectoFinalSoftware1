from django.shortcuts import render

# Create your views here.
def pomodoro(request):
    return render(request, 'pomodoro.html')