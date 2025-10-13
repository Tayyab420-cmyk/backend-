from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import BusRouteViewSet, HotelViewSet, BookingViewSet

router = DefaultRouter()
router.register(r'busroutes', BusRouteViewSet, basename='busroute')
router.register(r'hotels', HotelViewSet, basename='hotel')
router.register(r'bookings', BookingViewSet, basename='booking')

urlpatterns = [
    path('', include(router.urls)),
]