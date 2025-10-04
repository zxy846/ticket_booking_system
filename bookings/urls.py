from django.urls import path
from . import views

app_name = 'bookings'
urlpatterns = [
    path('create/<int:flight_id>/', views.booking_create, name='booking_create'),
    path('confirm/<str:ref>/', views.booking_confirm, name='booking_confirm'),
    path('manage/', views.my_bookings, name='my_bookings'),
]