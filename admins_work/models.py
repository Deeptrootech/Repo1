from django.contrib.auth.models import User
from django.db import models
from django.db.models import CASCADE


# Create your models here.
class Userprofile(models.Model):
    user = models.OneToOneField(User, on_delete=CASCADE)
    user_mobile = models.CharField(max_length=10)
    user_profile_photo = models.ImageField(upload_to='user_images/')
    user_address = models.CharField(max_length=20)
    user_postal_code = models.CharField(max_length=6)


Availability = [("Available", "Available"), ("NotAvailable", "NotAvailable")]
Types = [("AC", "AC"), ("NonAC", "NonAC")]


class Rooms(models.Model):
    room_name = models.CharField(max_length=20)
    room_status = models.CharField(max_length=20, choices=Availability)
    room_type = models.CharField(max_length=20, choices=Types)

    class Meta:
        ordering = ["id"]


class Customer(models.Model):
    customer_name = models.CharField(max_length=20)
    customer_age = models.IntegerField()
    customer_address = models.CharField(max_length=20)
    customer_mobile = models.CharField(max_length=20)


class ExtraServices(models.Model):
    service_name = models.CharField(max_length=20)
    service_price = models.DecimalField(max_digits=7, decimal_places=2)


class Booking(models.Model):
    user = models.ForeignKey(User, on_delete=CASCADE)
    customer = models.ForeignKey(Customer, on_delete=CASCADE)
    rooms = models.ManyToManyField(Rooms)
    extra_service = models.ManyToManyField(ExtraServices)
    CheckInTime = models.DateTimeField()
    CheckOutTime = models.DateTimeField()
