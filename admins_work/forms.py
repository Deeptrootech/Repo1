from django import forms
from django.contrib.auth.models import User

from .models import Userprofile, Rooms, Customer, ExtraServices, Booking


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ("username", "first_name", "last_name", "email")


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = Userprofile
        exclude = ("user",)

    def __init__(self, *args, **kwargs):
        super(UserProfileForm, self).__init__(*args, **kwargs)

        self.fields['user_mobile'].widget.attrs['class'] = 'form-control'
        self.fields['user_mobile'].widget.attrs['placeholder'] = 'Mobile:'
        self.fields['user_mobile'].label = ''
        self.fields[
            'user_mobile'].help_text = '<span class="form-text text-muted"><small>Required. Numbers only.</small></span>'


class RoomsForm(forms.ModelForm):
    class Meta:
        model = Rooms
        fields = "__all__"


class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = "__all__"


class ExtraServicesForm(forms.ModelForm):
    class Meta:
        model = ExtraServices
        fields = "__all__"


class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = "__all__"
