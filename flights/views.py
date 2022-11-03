from flights.serializers import BookingListSerializar, FlightListSerializer
from .models import Booking, Flight
from rest_framework.generics import ListAPIView

class FlightListView(ListAPIView):
    queryset = Flight.objects.all()
    serializer_class = FlightListSerializer


class UpcomingBookingListView(ListAPIView):
    queryset = Booking.objects.all()
    serializer_class = BookingListSerializar

class BookingListView(ListAPIView):
    queryset = Booking.objects.all()
    serializer_class = BookingListSerializar

