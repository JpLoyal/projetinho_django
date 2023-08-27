from django.shortcuts import render

# Create your views here.

rooms = [
    {'id': 1, 'name': 'Lets learn python!'},
    {'id': 2, 'name': 'Design with me'},
    {'id': 3, 'name': 'Frontend developers'},
]

def home(request):
    return render(request, 'base/home.html', {'exemplo': rooms})

def room(request):
    return render(request, 'base/room.html')