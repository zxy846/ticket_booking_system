from django.shortcuts import render

def order_list(request):
    return render(request, 'orders/order_list.html')

def order_detail(request, order_id):
    return render(request, 'orders/order_detail.html', {'order_id': order_id})

def order_cancel(request, order_id):
    return render(request, 'orders/order_cancel.html', {'order_id': order_id})

def order_payment(request, order_id):
    return render(request, 'orders/order_payment.html', {'order_id': order_id})

def payment_success(request):
    return render(request, 'orders/payment_success.html')