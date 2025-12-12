from django.contrib import admin
from .models import Passenger, Booking, BookingPassenger

@admin.register(Passenger)
class PassengerAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'passport_number', 'email']
    search_fields = ['first_name', 'last_name', 'passport_number']
    list_filter = ['date_of_birth']

@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ['booking_reference', 'user', 'flight', 'total_price', 'status', 'booking_date']
    list_filter = ['status', 'booking_date', 'flight']
    search_fields = ['booking_reference', 'user__username', 'flight__flight_number']
    date_hierarchy = 'booking_date'

@admin.register(BookingPassenger)
class BookingPassengerAdmin(admin.ModelAdmin):
    list_display = ['booking', 'passenger', 'seat_number']
    list_filter = ['booking__flight']