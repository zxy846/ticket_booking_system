from django.db import models
from django.contrib.auth.models import User

class Flight(models.Model):
    id = models.AutoField(primary_key=True)
    flight_number = models.CharField(max_length=10)
    departure_airport = models.CharField(max_length=3)
    arrival_airport = models.CharField(max_length=3)
    departure_time = models.DateTimeField()
    arrival_time = models.DateTimeField()
    total_seats = models.IntegerField()
    available_seats = models.IntegerField()

    class Meta:
        permissions = [
            ("can_view_flight", "Can view flight"),
            ("can_add_flight", "Can add flight"),
            ("can_change_flight", "Can change flight"),
            ("can_delete_flight", "Can delete flight"),
        ]


    def __str__(self):
        return f"{self.flight_number} ({self.departure_airport} -> {self.arrival_airport})"