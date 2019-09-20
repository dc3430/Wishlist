from django.shortcuts import render

from .models import Wish


def home( request):
    return render(request, 'home.html')
