
from rest_framework import serializers
from django.contrib.auth.models import User

from .models import Booking, Flight

class FlightListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Flight
        fields = ["id", "destination", "time","time","price"]


class BookingListSerializar(serializers.ModelSerializer):
    class Meta:
        model = Booking
        field = ["flight", "date", "id"]

class DetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        field = ["flight", "date", "id", "passengers"]

class RegisterSerialzer(serializers.ModelSerializer):
    password = serializers.CharField(write_only = True)
    class Meta:
        model = User
        fields = ["username", "password"]

    def create(self, validated_data):
        password = validated_data.pop('password')
        new_user = User(**validated_data)
        new_user.set_password(password)
        new_user.save()
        return new_user
