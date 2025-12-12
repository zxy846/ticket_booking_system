# views.py 修改后的内容
from django.shortcuts import render, get_object_or_404, redirect
from django.db.models import Q
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from .models import Flight
from .forms import FlightForm


# 登录视图 - 改为函数视图
def user_login(request):
    """
    用户登录视图
    """
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('flight_list')
    else:
        form = AuthenticationForm()

    return render(request, 'login.html', {'form': form})


# 登出视图 - 改为函数视图
def user_logout(request):
    """
    用户登出视图
    """
    if request.method == 'POST' or request.method == 'GET':  # 允许 GET 和 POST 请求
        logout(request)
        return redirect('login')
    return redirect('flight_list')


# 航班列表 - 需要登录和查看权限
@login_required
@permission_required('flights.can_view_flight', raise_exception=True)
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


# 航班详情 - 需要登录和查看权限
@login_required
@permission_required('flights.can_view_flight', raise_exception=True)
def flight_detail(request, id):
    flight = get_object_or_404(Flight, id=id)
    return render(request, 'flight_detail.html', {'flight': flight})


# 创建航班 - 需要登录和添加权限
@login_required
@permission_required('flights.can_add_flight', raise_exception=True)
def flight_create(request):
    if request.method == 'POST':
        form = FlightForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('flight_list')
    else:
        form = FlightForm()

    return render(request, 'flight_form.html', {
        'form': form,
        'title': 'Create a new flight'
    })


# 编辑航班 - 需要登录和修改权限
@login_required
@permission_required('flights.can_change_flight', raise_exception=True)
def flight_update(request, id):
    flight = get_object_or_404(Flight, id=id)

    if request.method == 'POST':
        form = FlightForm(request.POST, instance=flight)
        if form.is_valid():
            form.save()
            return redirect('flight_detail', id=flight.id)
    else:
        form = FlightForm(instance=flight)

    return render(request, 'flight_form.html', {
        'form': form,
        'title': 'Edit flight',
        'flight': flight
    })


# 删除航班 - 需要登录和删除权限
# flights/views.py
@login_required
@permission_required('flights.can_delete_flight', raise_exception=True)
def flight_delete(request, id):
    flight = get_object_or_404(Flight, id=id)

    if request.method == 'POST':
        flight.delete()
        messages.success(request, f'Flight {flight.flight_number} has been deleted successfully!')
        return redirect('flight_list')

    # 如果是GET请求，直接重定向到列表页（与passengers/tickets保持一致）
    messages.warning(request, 'Please use the delete form to delete flights.')
    return redirect('flight_list')

