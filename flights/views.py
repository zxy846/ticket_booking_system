from django.shortcuts import render

def flight_list(request):
    return render(request, 'flights/flight_list.html')

def flight_search(request):
    return render(request, 'flights/flight_search.html')

def flight_detail(request, flight_id):
    return render(request, 'flights/flight_detail.html', {'flight_id': flight_id})

def flight_book(request, flight_id):
    return render(request, 'flights/flight_book.html', {'flight_id': flight_id})