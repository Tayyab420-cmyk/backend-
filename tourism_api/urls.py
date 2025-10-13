from django.contrib import admin
from django.urls import path, include
from django.http import JsonResponse

def root_view(request):
    return JsonResponse({"message": "Welcome to the Tourism API. Use /api/busroutes/ or /api/hotels/."})

urlpatterns = [
    path('', root_view),  # Handle root URL
    path('admin/', admin.site.urls),
    path('api/', include('travel.urls')),
]