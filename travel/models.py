from django.db import models

class BusRoute(models.Model):
    from_city = models.CharField(max_length=100)
    to_city = models.CharField(max_length=100)
    departure_time = models.CharField(max_length=10)  # e.g., "08:00 AM"
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image_url = models.URLField(max_length=500)
    seats_available = models.IntegerField(default=40)  # Remove if not in original

    def __str__(self):
        return f"{self.from_city} to {self.to_city}"

class Hotel(models.Model):
    name = models.CharField(max_length=200)
    city = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    room_types = models.JSONField()  # e.g., ["Standard", "Deluxe"]
    image_url = models.URLField(max_length=500)
    rooms_available = models.IntegerField(default=10)  # Remove if not in original

    def __str__(self):
        return self.name

class Booking(models.Model):
    TYPE_CHOICES = [
        ('bus', 'Bus'),
        ('hotel', 'Hotel'),
    ]
    user = models.CharField(max_length=100)  # Reverted to CharField
    type = models.CharField(max_length=10, choices=TYPE_CHOICES)
    details = models.JSONField()
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.type} booking for {self.user} at {self.created_at}"