# flights/views.py
from django.shortcuts import render, get_object_or_404
from .models import Flight
from django.utils import timezone
from django.shortcuts import render, redirect


def flight_home(request):
    """航班搜索首页 - 集成搜索功能"""
    flights = None
    search_params = {}

    # 检查是否有搜索参数
    if request.method == 'GET' and any(key in request.GET for key in ['dep', 'arr', 'date']):
        dep = request.GET.get('dep', '')
        arr = request.GET.get('arr', '')
        date = request.GET.get('date', '')

        # 如果有搜索参数，重定向到结果页面
        if dep or arr or date:
            return redirect('flights:flight_results') + f'?dep={dep}&arr={arr}&date={date}'

    # 没有搜索时显示首页
    return render(request, 'flights/home.html')


def flight_results(request):
    """搜索结果页面"""
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