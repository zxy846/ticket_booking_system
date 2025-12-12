from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('', views.flight_list, name='flight_list'),
    path('flight/<int:id>/', views.flight_detail, name='flight_detail'),
    path('flight/create/', views.flight_create, name='flight_create'),
    path('flight/<int:id>/update/', views.flight_update, name='flight_update'),
    path('flight/<int:id>/delete/', views.flight_delete, name='flight_delete'),
]