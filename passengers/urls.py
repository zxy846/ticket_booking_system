from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.passenger_register, name='passenger_register'),
    path('login/', views.passenger_login, name='passenger_login'),
    path('logout/', views.passenger_logout, name='passenger_logout'),
    path('profile/', views.passenger_profile, name='passenger_profile'),
    path('profile/edit/', views.passenger_profile_edit, name='passenger_profile_edit'),
]