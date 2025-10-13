from rest_framework import viewsets
from rest_framework.permissions import AllowAny
from .models import BusRoute, Hotel, Booking
from .serializers import BusRouteSerializer, HotelSerializer, BookingSerializer

class BusRouteViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = BusRoute.objects.all()
    serializer_class = BusRouteSerializer
    permission_classes = [AllowAny]

class HotelViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Hotel.objects.all()
    serializer_class = HotelSerializer
    permission_classes = [AllowAny]

class BookingViewSet(viewsets.ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
    permission_classes = [AllowAny]