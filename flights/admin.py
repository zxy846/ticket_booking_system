from django.contrib import admin
from .models import Airport, Flight

@admin.register(Airport)
class AirportAdmin(admin.ModelAdmin):
    list_display = ['code', 'city']
    search_fields = ['code', 'city']
    list_filter = ['city']

@admin.register(Flight)
class FlightAdmin(admin.ModelAdmin):
    list_display = ['flight_number', 'departure_airport', 'arrival_airport', 'departure_time', 'price']
    list_filter = ['departure_airport', 'arrival_airport', 'departure_time']
    search_fields = ['flight_number', 'departure_airport__city', 'arrival_airport__city']
    date_hierarchy = 'departure_time'