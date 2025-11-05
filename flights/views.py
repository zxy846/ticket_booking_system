from django.shortcuts import render, get_object_or_404, redirect
from django.db.models import Q
from django.contrib import messages
from .models import Flight
from .forms import FlightForm


def flight_list(request):
    flights = Flight.objects.all()

    # 搜索功能
    search_query = request.GET.get('search', '')
    if search_query:
        flights = flights.filter(
            Q(flight_number__icontains=search_query) |
            Q(departure_airport__icontains=search_query) |
            Q(arrival_airport__icontains=search_query)
        )

    return render(request, 'flight_list.html', {
        'flights': flights,
        'search_query': search_query
    })


def flight_detail(request, id):
    flight = get_object_or_404(Flight, id=id)
    return render(request, 'flight_detail.html', {'flight': flight})


def flight_create(request):
    if request.method == 'POST':
        form = FlightForm(request.POST)
        if form.is_valid():
            flight = form.save()
            messages.success(request, f'Flight {flight.flight_number} created successfully!')
            return redirect('flight_list')
    else:
        form = FlightForm()

    return render(request, 'flight_form.html', {
        'form': form,
        'title': 'Create New Flight'
    })


def flight_update(request, id):
    flight = get_object_or_404(Flight, id=id)

    if request.method == 'POST':
        form = FlightForm(request.POST, instance=flight)
        if form.is_valid():
            form.save()
            messages.success(request, f'Flight {flight.flight_number} updated successfully!')
            return redirect('flight_detail', id=flight.id)
    else:
        form = FlightForm(instance=flight)

    return render(request, 'flight_form.html', {
        'form': form,
        'title': 'Edit Flight',
        'flight': flight
    })


def flight_delete(request, id):
    flight = get_object_or_404(Flight, id=id)

    if request.method == 'POST':
        flight_number = flight.flight_number
        flight.delete()
        messages.success(request, f'Flight {flight_number} deleted successfully!')
        return redirect('flight_list')

    # 如果是GET请求，直接重定向到列表页
    return redirect('flight_list')