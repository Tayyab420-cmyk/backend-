from rest_framework import serializers
from .models import BusRoute, Hotel, Booking

class BusRouteSerializer(serializers.ModelSerializer):
    class Meta:
        model = BusRoute
        fields = ['id', 'from_city', 'to_city', 'departure_time', 'price', 'seats_available', 'image_url']

class HotelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hotel
        fields = ['id', 'name', 'city', 'price', 'room_types', 'image_url', 'rooms_available']

class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = ['id', 'user', 'type', 'details', 'total_price', 'created_at']