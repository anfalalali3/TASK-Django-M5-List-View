from flights.serializers import BookingListSerializar, FlightListSerializer, RegisterSerialzer,DetailSerializer
from .models import Booking, Flight
from rest_framework.generics import ListAPIView, RetrieveAPIView , CreateAPIView, UpdateAPIView, DestroyAPIView

class FlightListView(ListAPIView):
    queryset = Flight.objects.all()
    serializer_class = FlightListSerializer


class UpcomingBookingListView(ListAPIView):
    queryset = Booking.objects.all()
    serializer_class = BookingListSerializar

class BookingListView(ListAPIView):
    queryset = Booking.objects.all()
    serializer_class = BookingListSerializar

class DetailView(RetrieveAPIView):
    queryset = Booking.objects.all()
    serializer_class = DetailSerializer
    lookup_field = 'id'
    lookup_url_kwarg = 'object_id'

class UserRegisterAPIView(CreateAPIView):
    serializer_class = RegisterSerialzer


class UpdateView(UpdateAPIView):
    queryset = Booking.objects.all()
    serializer_class = RegisterSerialzer
    lookup_field = 'id'
    lookup_url_kwarg = 'object_id'


class DeleteView(DestroyAPIView):
    queryset = Booking.objects.all()
    serializer_class = BookingListSerializar
    lookup_field = 'id'
    lookup_url_kwarg = 'object_id'
    





