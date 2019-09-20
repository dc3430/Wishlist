from django.urls import path
from . import views

urlpatterns = [
    path('', views.wish_index, name='wish_index'),
    path('add/', views.WishCreate.as_view(), name='wish_create'),
    path('delete/<int:wish_id>', views.WishDelete.as_view(), name='wish_delete'),
]

