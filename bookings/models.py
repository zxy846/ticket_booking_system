from django.db import models
from django.contrib.auth.models import User

# 使用字符串引用避免循环导入
class Passenger(models.Model):
    first_name = models.CharField(max_length=100)
    last_name  = models.CharField(max_length=100)
    date_of_birth = models.DateField()
    passport_number = models.CharField(max_length=20, unique=True)
    email = models.EmailField()
    phone = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Booking(models.Model):
    STATUS = [
        ('confirmed', '已确认'),
        ('cancelled', '已取消'),
        ('pending', '待支付'),
    ]
    booking_reference = models.CharField(max_length=10, unique=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    flight = models.ForeignKey('flights.Flight', on_delete=models.CASCADE)  # 使用字符串引用
    passengers = models.ManyToManyField(Passenger, through='BookingPassenger')
    booking_date = models.DateTimeField(auto_now_add=True)
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=20, choices=STATUS, default='confirmed')

    def __str__(self):
        return f"订单 {self.booking_reference}"


class BookingPassenger(models.Model):
    booking = models.ForeignKey(Booking, on_delete=models.CASCADE)
    passenger = models.ForeignKey(Passenger, on_delete=models.CASCADE)
    seat_number = models.CharField(max_length=10, blank=True)
    special_requests = models.TextField(blank=True)

    class Meta:
        unique_together = ('booking', 'passenger')