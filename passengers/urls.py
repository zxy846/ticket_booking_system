from django.urls import path
from . import views

urlpatterns = [
    path('', views.passenger_list, name='passenger_list'),
    path('<int:id>/', views.passenger_detail, name='passenger_detail'),
    path('create/', views.passenger_create, name='passenger_create'),
    path('<int:id>/update/', views.passenger_update, name='passenger_update'),
    path('<int:id>/delete/', views.passenger_delete, name='passenger_delete'),
]