from django.urls import path
from . import views

urlpatterns = [
    path('', views.order_list, name='order_list'),
    path('<int:order_id>/', views.order_detail, name='order_detail'),
    path('<int:order_id>/cancel/', views.order_cancel, name='order_cancel'),
    path('<int:order_id>/payment/', views.order_payment, name='order_payment'),
    path('payment/success/', views.payment_success, name='payment_success'),
]