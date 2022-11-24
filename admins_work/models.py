"""
Classes that acts as database tables
when user submits record using this file
we can access database and make crud operation
"""

from django.contrib.auth.models import User
from django.db import models
from django.db.models import CASCADE, PROTECT


# Create your models here.
class Userprofile(models.Model):
    """
    Data like mobile,address,postalcode entered by user
    of website will be saved here
    """
    user = models.OneToOneField(User, on_delete=CASCADE, null=True, blank=True)
    user_mobile = models.CharField(max_length=10)
    user_profile_photo = models.ImageField(upload_to='user_images/',
                                           default="default.jpg")
    user_address = models.CharField(max_length=20)
    user_postal_code = models.CharField(max_length=6)


Availability = [("Available", "Available"), ("NotAvailable", "NotAvailable")]
Types = [("AC", "AC"), ("NonAC", "NonAC")]


class Rooms(models.Model):
    """
    Data related to rooms entered by admins
    will be saved here
    """
    room_name = models.CharField(max_length=20)
    room_status = models.CharField(max_length=20, choices=Availability)
    room_type = models.CharField(max_length=20, choices=Types)

    class Meta:
        """
        Model Meta is basically used to change
        the behavior of your model fields like
        changing order options,verbose_name,
        and a lot of other option
        """

        ordering = ["id"]

    def __str__(self):
        """
        Used to display each created data(row) with its specific name
        """
        return self.room_name + "(" + self.room_type + ")"


class Customer(models.Model):
    """
    This model is about data of customers who will book service
    this data will be entered by admins because for backend side
    created application admins will book service on behalf of
    users(customer)
    """
    customer_name = models.CharField(max_length=20)
    customer_age = models.IntegerField()
    customer_address = models.CharField(max_length=20)
    customer_mobile = models.CharField(max_length=10)

    def __str__(self):
        """
        Used to display each created data(row) with its specific name
        """
        return self.customer_name


class ExtraServices(models.Model):
    """
    Services apart from rooms if customer wants to take for that
    this table is used
    """
    service_name = models.CharField(max_length=20)
    service_price = models.DecimalField(max_digits=7, decimal_places=2)

    def __str__(self):
        """
        Used to display each created data(row) with its specific name
        """
        return self.service_name


class Booking(models.Model):
    """
    Rooms that booked by user(customer) with their extra services
    if any that to store that record this table is used
    """
    user = models.ForeignKey(User, on_delete=PROTECT)
    customer = models.ForeignKey(Customer, on_delete=PROTECT)
    rooms = models.ManyToManyField(Rooms)
    extra_service = models.ManyToManyField(ExtraServices, blank=True, null=True)
    CheckInDate = models.DateField()
    CheckOutDate = models.DateField()
