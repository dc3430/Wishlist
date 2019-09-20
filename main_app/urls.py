from django.urls import path
from . import views

urlpatterns = [
    path('', views.wish_index, name='wish_index'),
    # path('add/', views.Wish.as_index(), name='add'),
    # path('delete/<int:item_id>', views.delete, name='delete'),
]