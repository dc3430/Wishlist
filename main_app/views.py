from django.shortcuts import render

from .models import Wish


def wish_index(request):
  wishs = Wish.objects.all()
  return render(request, 'wishs/index.html', { 'wishs': wishs })


