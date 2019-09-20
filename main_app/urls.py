from django.urls import path
from . import views

urlpatterns= [
    path('', views.index, name='index'),
    path('add/',views.WishCreate.as_view(), name='wish_create'),
    path('<int:pk>/delete/', views.WishDelete.as_view(), name='wish_delete'),
]