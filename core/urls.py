from django.urls import path
from . import views

urlpatterns = [
    path('create-trip/', views.create_trip, name='create_trip'),
    path('driver-dashboard/', views.driver_dashboard, name='driver_dashboard'),
    path('trip/<int:trip_id>/', views.trip_detail, name='trip_detail'),
]
