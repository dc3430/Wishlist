from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    # path('wishs/', views.wishs_index, name='index'),
    # path('wishs/<int:wish_id>/', views.wishs_detail, name='detail'),
    # path('wishs/create/', views.WishCreate.as_view(), name='wishs_create'),
    # path('wishs/<int:pk>/update/', views.WishUpdate.as_view(), name='wishs_update'),
    # path('wishs/<int:pk>/delete/', views.WishDelete.as_view(), name='wishs_delete'),
]