from django.contrib import admin
from .models import CustomUser, Trip

@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'role', 'phone')
    search_fields = ('username', 'email')

@admin.register(Trip)
class TripAdmin(admin.ModelAdmin):
    list_display = ('id', 'passenger', 'driver', 'status', 'from_city', 'to_city')
    list_filter = ('status',)
