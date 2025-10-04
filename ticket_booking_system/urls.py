from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('pages.urls')),
    path('flights/', include('flights.urls')),
    path('bookings/', include('bookings.urls')),
]