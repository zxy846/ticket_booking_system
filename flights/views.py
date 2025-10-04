from django.shortcuts import render, get_object_or_404
from .models import Flight
from django.utils import timezone
from django.shortcuts import render

def flight_home(request):
    """航班搜索首页"""
    return render(request, 'flights/home.html')
def flight_search(request):
    """ 接收出发地、目的地、日期 """
    return render(request, 'flights/search.html', {})


def flight_results(request):
    """ 搜索结果 + 排序/筛选 """
    dep = request.GET.get('dep', '')
    arr = request.GET.get('arr', '')
    date = request.GET.get('date', '')

    flights = Flight.objects.all()

    # 应用搜索过滤
    if dep:
        flights = flights.filter(departure_airport__city__icontains=dep)
    if arr:
        flights = flights.filter(arrival_airport__city__icontains=arr)
    if date:
        try:
            flights = flights.filter(departure_time__date=date)
        except:
            pass

    return render(request, 'flights/results.html', {
        'flights': flights,
        'search_params': {'dep': dep, 'arr': arr, 'date': date}
    })


def flight_detail(request, flight_id):
    flight = get_object_or_404(Flight, id=flight_id)
    return render(request, 'flights/detail.html', {'flight': flight})