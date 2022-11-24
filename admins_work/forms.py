"""
File is used where you want to work with form with database
"""

from datetime import datetime
from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.core.validators import validate_email
from django.db.models import Q

from .models import Userprofile, Rooms, Customer, ExtraServices, Booking


class UserForm(forms.ModelForm):
    """
    This class connects User form of django authentication
    """

    class Meta:
        """
        Model Meta is basically used to change
        the behavior of your model fields like
        changing order options,verbose_name,
        and a lot of other option
        """
        model = User
        fields = ("username", "first_name", "last_name", "email")

    def __init__(self, *args, **kwargs):
        """
        Init method of forms
        """
        super(UserForm, self).__init__(*args, **kwargs)

        for each_field in self.fields:
            self.fields[each_field].widget.attrs['class'] = 'form-control'

    def clean(self):
        """
        Used for validation
        :return: cleaned data
        """
        user_mail = self.cleaned_data.get('email')
        validate_email(user_mail)


class UserProfileForm(forms.ModelForm):
    """
    Connects userprofile model to manipulate its fields
    """

    class Meta:
        """
        Model Meta is basically used to change
        the behavior of your model fields like
        changing order options,verbose_name,
        and a lot of other option
        """
        model = Userprofile
        exclude = ("user",)

    def __init__(self, *args, **kwargs):
        """
        Init method of forms
        """
        super(UserProfileForm, self).__init__(*args, **kwargs)

        for each_field in self.fields:
            self.fields[each_field].widget.attrs['class'] = 'form-control'


class RoomsForm(forms.ModelForm):
    """
    Class is used for work with room model
    """

    class Meta:
        """
        Model Meta is basically used to change
        the behavior of your model fields like
        changing order options,verbose_name,
        and a lot of other option
        """
        model = Rooms
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        """
        Init method of forms
        """
        super(RoomsForm, self).__init__(*args, **kwargs)

        for each_field in self.fields:
            self.fields[each_field].widget.attrs['class'] = 'form-control'


class CustomerForm(forms.ModelForm):
    """
    Class is used for work with customer model
    """

    class Meta:
        """
        Model Meta is basically used to change
        the behavior of your model fields like
        changing order options,verbose_name,
        and a lot of other option
        """
        model = Customer
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        """
        Init method of forms
        """
        super(CustomerForm, self).__init__(*args, **kwargs)

        for each_field in self.fields:
            self.fields[each_field].widget.attrs['class'] = 'form-control'


class ExtraServicesForm(forms.ModelForm):
    """
    Class is used for work with extraservice model
    """

    class Meta:
        """
        Model Meta is basically used to change
        the behavior of your model fields like
        changing order options,verbose_name,
        and a lot of other option
        """
        model = ExtraServices
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        """
        Init method of forms
        """
        super(ExtraServicesForm, self).__init__(*args, **kwargs)

        for each_field in self.fields:
            self.fields[each_field].widget.attrs['class'] = 'form-control'


class BookingForm(forms.ModelForm):
    """
    Class is used for work with booking model
    """

    class Meta:
        """
        Model Meta is basically used to change
        the behavior of your model fields like
        changing order options,verbose_name,
        and a lot of other option
        """
        model = Booking
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        """
        Init method of forms
        """
        super(BookingForm, self).__init__(*args, **kwargs)

        for each_field in self.fields:
            self.fields[each_field].widget.attrs['class'] = 'form-control'

        if 'instance' not in kwargs.keys():
            rooms_to_be_displayed = []
        else:
            rooms_to_be_displayed = kwargs['instance'].rooms.all()
        self.fields['rooms'].queryset = Rooms.objects.filter(
            Q(room_status="Available") |
            Q(id__in=[my_room.id for my_room in rooms_to_be_displayed]))

    def clean(self):
        """
        Used for validation
        :return: cleaned data
        """
        checkin = self.cleaned_data.get('CheckInDate')
        checkout = self.cleaned_data.get('CheckOutDate')
        if checkin > checkout:
            raise ValidationError("checked out before checkin")

        if checkin < datetime.now().date():
            err = "Please add future date and time for checkin"
            self.add_error("CheckInDate", err)
        if checkout < datetime.now().date():
            err = "Please add future date and time for checkout"
            self.add_error("CheckOutDate", err)
