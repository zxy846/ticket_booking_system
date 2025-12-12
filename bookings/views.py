from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from flights.models import Flight
from .models import Booking, Passenger
from .forms import PassengerForm
import uuid

@login_required
def booking_create(request, flight_id):
    flight = get_object_or_404(Flight, id=flight_id)
    if request.method == 'POST':
        form = PassengerForm(request.POST)
        if form.is_valid():
            passenger = form.save()
            booking = Booking.objects.create(
                user=request.user,
                flight=flight,
                total_price=flight.price,   # 简化处理
                booking_reference=str(uuid.uuid4()).upper()[:8]
            )
            booking.passengers.add(passenger)   # 多对多关系
            return redirect('bookings:booking_confirm', ref=booking.booking_reference)
    else:
        form = PassengerForm()
    return render(request, 'bookings/create.html', {'form': form})

def booking_confirm(request, ref):
    booking = get_object_or_404(Booking, booking_reference=ref)
    return render(request, 'bookings/confirm.html', {'booking': booking})

@login_required
def my_bookings(request):
    bookings = Booking.objects.filter(user=request.user)
    return render(request, 'bookings/manage.html', {'bookings': bookings})