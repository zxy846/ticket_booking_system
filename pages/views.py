from django.shortcuts import render, redirect
from django.utils import timezone
from django.shortcuts import render

def home(request):
    if request.method == 'POST' or request.GET.get('dep'):
        # 如果有搜索参数，重定向到航班搜索结果
        dep = request.POST.get('dep') or request.GET.get('dep')
        arr = request.POST.get('arr') or request.GET.get('arr')
        date = request.POST.get('date') or request.GET.get('date')

        if dep and arr and date:
            return redirect(f"/flights/results/?dep={dep}&arr={arr}&date={date}")

    return render(request, 'pages/home.html', {})

def about(request):
    return render(request, 'pages/about.html', {})
