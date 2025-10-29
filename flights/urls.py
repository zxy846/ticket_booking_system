from django.urls import path
from . import views

urlpatterns = [
    path('', views.flight_list, name='flight_list'),
    path('search/', views.flight_search, name='flight_search'),
    path('<int:flight_id>/', views.flight_detail, name='flight_detail'),
    path('<int:flight_id>/book/', views.flight_book, name='flight_book'),
]