from django.contrib import admin
from .models import Flight

@admin.register(Flight)
class FlightAdmin(admin.ModelAdmin):
    list_display = ['flight_number', 'departure_airport', 'arrival_airport', 'departure_time', 'available_seats']
    list_filter = ['departure_airport', 'arrival_airport']
    search_fields = ['flight_number']