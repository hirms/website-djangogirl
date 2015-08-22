# trips/views.py
from datetime import datetime
#from django.http import HttpResponse
from django.shortcuts import render

def hello_world(request):
    return render(request, 'hello_world.html', {'current_time':datetime.now()})
