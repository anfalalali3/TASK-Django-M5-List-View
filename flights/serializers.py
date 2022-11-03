from dataclasses import field
from pyexpat import model
from statistics import mode
from rest_framework import serializers

from .models import Booking, Flight

class FlightListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Flight
        fields = ["id", "destination", "time","time","price"]


class BookingListSerializar(serializers.ModelSerializer):
    class Meta:
        model = Booking
        field = ["flight", "date", "id"]