from django.contrib import admin
from .models import BusRoute, Hotel, Booking

@admin.register(BusRoute)
class BusRouteAdmin(admin.ModelAdmin):
    list_display = ['from_city', 'to_city', 'seats_available']

@admin.register(Hotel)
class HotelAdmin(admin.ModelAdmin):
    list_display = ['name', 'city', 'rooms_available']

@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ['user', 'type', 'total_price', 'created_at']