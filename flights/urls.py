from django.urls import path
from . import views

app_name = 'flights'
urlpatterns = [
    path('', views.flight_home, name='flight_home'),
    path('results/', views.flight_results, name='flight_results'),
    path('<int:flight_id>/', views.flight_detail, name='flight_detail'),
]