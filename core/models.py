from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    """Кастомная модель пользователя с ролями"""
    ROLES = (
        ('ADMIN', 'Администратор'),
        ('DRIVER', 'Водитель'),
        ('PASSENGER', 'Пассажир'),
    )
    role = models.CharField(
        max_length=10, 
        choices=ROLES, 
        default='PASSENGER'
    )
    phone = models.CharField(max_length=20)

class Trip(models.Model):
    """Модель поездки"""
    STATUS_CHOICES = (
        ('PENDING', 'В ожидании'),
        ('ACCEPTED', 'Принят'),
        ('COMPLETED', 'Завершен'),
    )
    passenger = models.ForeignKey(
        CustomUser, 
        on_delete=models.CASCADE,
        related_name='passenger_trips'
    )
    driver = models.ForeignKey(
        CustomUser,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='driver_trips'
    )
    from_city = models.CharField(max_length=100)
    to_city = models.CharField(max_length=100)
    # ... остальные поля ...
