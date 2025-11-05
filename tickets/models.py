from django.db import models

class Ticket(models.Model):
    STATUS_CHOICES = [
        ('confirmed', 'Confirmed'),
        ('cancelled', 'Cancelled'),
    ]

    id = models.AutoField(primary_key=True)
    flight = models.ForeignKey('flights.Flight', on_delete=models.CASCADE)  # 使用字符串引用
    passenger = models.ForeignKey('passengers.Passenger', on_delete=models.CASCADE)  # 使用字符串引用
    seat_number = models.CharField(max_length=5)
    booking_reference = models.CharField(max_length=10, unique=True)
    price = models.FloatField()
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='confirmed')

    def __str__(self):
        return f"Ticket {self.booking_reference}"