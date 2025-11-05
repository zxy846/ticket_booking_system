from django.shortcuts import render, get_object_or_404, redirect
from django.db.models import Q
from django.contrib import messages
from .models import Passenger
from .forms import PassengerForm


def passenger_list(request):
    passengers = Passenger.objects.all()

    # 搜索功能
    search_query = request.GET.get('search', '')
    if search_query:
        passengers = passengers.filter(
            Q(first_name__icontains=search_query) |
            Q(last_name__icontains=search_query) |
            Q(email__icontains=search_query) |
            Q(phone_number__icontains=search_query)
        )

    return render(request, 'passenger_list.html', {
        'passengers': passengers,
        'search_query': search_query
    })


def passenger_detail(request, id):
    passenger = get_object_or_404(Passenger, id=id)
    return render(request, 'passenger_detail.html', {'passenger': passenger})


def passenger_create(request):
    if request.method == 'POST':
        form = PassengerForm(request.POST)
        if form.is_valid():
            passenger = form.save()
            messages.success(request, f'Passenger {passenger.first_name} {passenger.last_name} created successfully!')
            return redirect('passenger_detail', id=passenger.id)
    else:
        form = PassengerForm()

    return render(request, 'passenger_form.html', {
        'form': form,
        'title': 'Add Passenger'
    })


def passenger_update(request, id):
    passenger = get_object_or_404(Passenger, id=id)

    if request.method == 'POST':
        form = PassengerForm(request.POST, instance=passenger)
        if form.is_valid():
            form.save()
            messages.success(request, f'Passenger {passenger.first_name} {passenger.last_name} updated successfully!')
            return redirect('passenger_detail', id=passenger.id)
    else:
        form = PassengerForm(instance=passenger)

    return render(request, 'passenger_form.html', {
        'form': form,
        'title': 'Edit Passenger',
        'passenger': passenger
    })


def passenger_delete(request, id):
    passenger = get_object_or_404(Passenger, id=id)

    if request.method == 'POST':
        passenger_name = f"{passenger.first_name} {passenger.last_name}"
        passenger.delete()
        messages.success(request, f'Passenger {passenger_name} deleted successfully!')
        return redirect('passenger_list')

    # 如果是GET请求，直接重定向到列表页
    return redirect('passenger_list')