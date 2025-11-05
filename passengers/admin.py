from django.contrib import admin
from .models import Passenger


@admin.register(Passenger)
class PassengerAdmin(admin.ModelAdmin):
    list_display = ['id', 'first_name', 'last_name', 'email', 'phone_number']
    list_display_links = ['id', 'first_name']
    search_fields = ['first_name', 'last_name', 'email', 'phone_number']
    list_filter = ['first_name', 'last_name']
    list_per_page = 20



