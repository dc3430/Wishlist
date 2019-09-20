from django.shortcuts import render

from .models import Wish

from django.views.generic.edit import CreateView, DeleteView

def wish_index(request):
  wishs = Wish.objects.all()
  return render(request, 'wishs/index.html', { 'wishs': wishs })



class WishCreate(CreateView):
    model = Wish
    fields = '__all__'
    success_url = '/'

class WishDelete(DeleteView):
    model = Wish
    success_url = '/'




