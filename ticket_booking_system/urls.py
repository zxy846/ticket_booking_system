from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('flights/', include('flights.urls')),
    path('bookings/', include('bookings.urls')),
    path('', RedirectView.as_view(pattern_name='flights:flight_home')),
]