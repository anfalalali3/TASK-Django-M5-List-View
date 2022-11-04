"""airport URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from flights.views import FlightListView, BookingListView, UpcomingBookingListView, DetailView, UserRegisterAPIView,UpdateView, DeleteView

urlpatterns = [
    path("admin/", admin.site.urls),
    path("flights/", FlightListView.as_view(), name= "flight_list"),
    path("Booking/", BookingListView.as_view(), name= "booking_list"),
    path("UpcomingBooking/", UpcomingBookingListView.as_view(), name= "UpcomingBooking"),
    path('detail/<int:object_id>/', DetailView.as_view(), name='detail'),
    path('Register/', UserRegisterAPIView.as_view(), name='Register'),
    path('Update/<int:object_id>/', UpdateView.as_view(), name='update'),
    path('Delete/<int:object_id>/', DeleteView.as_view(), name='Delete')
]
