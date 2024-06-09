from django.shortcuts import render
from .models import Return

def return_list(request):
    returns = Return.objects.all()
    return render(request, 'return_list.html', {'returns': returns})
