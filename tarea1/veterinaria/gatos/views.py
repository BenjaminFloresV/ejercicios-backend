from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render(request, 'gatos/index.html', {
        'welcome_msg' : 'Hola, un lindo gatito te da la bienvenida'
    })

def add_cat(request):
    if request.method == 'POST':
        # Logic to save a new cat
        pass
    elif request.method == 'GET':
        # Logic to show the form
        pass

def get_cats(request):
    # Logic to show all cats
    pass