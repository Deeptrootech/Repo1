"""
Django views are Python functions that takes http requests
and returns http response, like HTML documents
"""
import datetime
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.shortcuts import render, redirect, get_object_or_404

from .forms import UserProfileForm, UserForm, RoomsForm, \
    ExtraServicesForm, BookingForm, CustomerForm
from .models import Customer, Rooms, ExtraServices, Booking


# Create your views here.
@login_required(login_url='/login_form')
def user_index(request):
    """
    Called when user index page rendered and returns user_index page
    :param request:
    :return:
    """
    if request.POST:
        user_profile_form = UserProfileForm(data=request.POST, instance=request.user.userprofile,
                                            files=request.FILES)
        user_form = UserForm(request.POST, instance=request.user)
        print(request.POST)
        print(user_profile_form)
        print(user_profile_form.cleaned_data)
        if user_profile_form.is_valid() and user_form.is_valid():
            user_profile_form.save()
            user_form.save()
            UserProfileForm()
            UserForm()
            return redirect("user_index")
        else:
            print("Form is not valid")
            return redirect("user_index")
    user_profile_form = UserProfileForm(instance=request.user.userprofile)
    user_form = UserForm(instance=request.user)
    photo_url = request.user.userprofile.user_profile_photo
    return render(request, "user_templates/user_index.html",
                  {"user_form": user_form, "user_profile_form": user_profile_form,
                   "photo_url": photo_url})


@login_required(login_url='/login_form')
def view_rooms(request):
    """
    Called when user request for view all rooms
    Returns my_rooms page pagination implemented here
    :param request:
    :return:
    """
    all_rooms = Rooms.objects.all()
    my_pagination = Paginator(all_rooms, 5)

    page_number = request.GET.get('page', 1)
    page_obj = my_pagination.page(page_number)
    return render(request, "user_templates/my_rooms.html", {"page_obj": page_obj})


@login_required(login_url='/login_form')
def add_rooms(request):
    """
    Called when user request for add new rooms
    returns view_rooms page
    :param request:
    :return:
    """
    if request.POST:
        rooms_form = RoomsForm(request.POST)
        if rooms_form.is_valid():
            rooms_form.save()
            RoomsForm()
            return redirect(view_rooms)
    else:
        rooms_form = RoomsForm()
    return render(request, "user_templates/add_rooms.html", {"rooms_form": rooms_form})


@login_required(login_url='/login_form')
def update_rooms(request, update_id):
    """ room_tobe_updated and initial_instance same j 6e
    to pan room_update_instance j work kare 6e olu nai why ????"""

    room_tobe_updated = get_object_or_404(Rooms, pk=update_id)
    if request.POST:
        room_form = RoomsForm(request.POST, instance=room_tobe_updated)
        if room_form.is_valid():
            room_update_instance = get_object_or_404(Rooms, pk=update_id)
            flag = 0
            if room_update_instance.room_status == "NotAvailable" and room_form.cleaned_data[
                "room_status"] == "Available":
                for each_booking in room_update_instance.booking_set.all():
                    if each_booking.CheckOutDate >= datetime.datetime.now().date():
                        flag = 1
            if not flag:
                room_form.save()
            else:
                print("status not updated it used in booking")
            return redirect(view_rooms)
    else:
        room_form = RoomsForm(instance=room_tobe_updated)
    return render(request, "user_templates/update_room.html", {"room_form": room_form,
                                                               "update_id": update_id})


@login_required(login_url='/login_form')
def delete_rooms(request, delete_id):
    """
    Called when user wants to delete any room
    returns view_rooms page
    :param request:
    :param delete_id:
    :return:
    """
    room_tobe_deleted = get_object_or_404(Rooms, pk=delete_id)
    room_total_bookings = room_tobe_deleted.booking_set.all()
    if room_total_bookings:
        print("You Can not delete Room.. it used")
    else:
        room_tobe_deleted.delete()
    return redirect(view_rooms)


@login_required(login_url='/login_form')
def view_extra_services(request):
    """
    Called to get extra_services from database
    and display at my_extra_services page
    :param request:
    :return:
    """
    all_services = ExtraServices.objects.all()
    my_pagination = Paginator(all_services, 5)

    page_number = request.GET.get('page', 1)
    page_obj = my_pagination.page(page_number)
    return render(request, "user_templates/my_extra_services.html", {"page_obj": page_obj})


@login_required(login_url='/login_form')
def add_extra_services(request):
    """
    Called to add new extra_service
    and display at add_extra_services page
    :param request:
    :return:
    """
    if request.POST:
        extra_service_form = ExtraServicesForm(request.POST)
        if extra_service_form.is_valid():
            extra_service_form.save()
            ExtraServicesForm()
            return redirect(view_extra_services)
    else:
        extra_service_form = ExtraServicesForm()
    return render(request, "user_templates/add_extra_services.html",
                  {"extra_service_form": extra_service_form})


@login_required(login_url='/login_form')
def update_extra_services(request, update_id):
    """
    Called to update extra service
    :param request:
    :param update_id:
    :return:
    """
    services_tobe_updated = get_object_or_404(ExtraServices, pk=update_id)
    if request.POST:
        services_form = ExtraServicesForm(request.POST, instance=services_tobe_updated)
        if services_form.is_valid():
            services_form.save()
            return redirect(view_extra_services)
    else:
        services_form = ExtraServicesForm(instance=services_tobe_updated)
    return render(request, "user_templates/update_service.html",
                  {"services_form": services_form, "update_id": update_id})


@login_required(login_url='/login_form')
def delete_extra_services(request, delete_id):
    """
    Called when user want to delete extra service
    :param request:
    :param delete_id:
    :return: redirects at view_extra_services page
    """
    services_tobe_deleted = get_object_or_404(ExtraServices, pk=delete_id)

    service_used_bookings = services_tobe_deleted.booking_set.all()
    if service_used_bookings:
        print("You Can not delete Service.. it used")
    else:
        services_tobe_deleted.delete()
    return redirect(view_extra_services)


@login_required(login_url='/login_form')
def view_booking(request):
    """
    Called when user want to see all bookings
    :param request:
    :return:
    """
    all_bookings = Booking.objects.all()
    my_pagination = Paginator(all_bookings, 5)
    page_number = request.GET.get('page', 1)
    page_obj = my_pagination.page(page_number)
    return render(request, "user_templates/my_bookings.html", {"page_obj": page_obj})


@login_required(login_url='/login_form')
def add_booking(request):
    """
    Called when user want to create new bookings
    :param request:
    :return:
    """
    if request.POST:
        booking_form = BookingForm(request.POST)
        if booking_form.is_valid():
            booking_form.save()

            """ Updating in Rooms db that booked room is non-available"""
            selected_rooms = booking_form.cleaned_data['rooms']
            for my_rooms in selected_rooms:
                get_room_form_db = Rooms.objects.get(id=my_rooms.id)
                get_room_form_db.room_status = "NotAvailable"
                get_room_form_db.save()
            return redirect(view_booking)
    else:
        booking_form = BookingForm()
    return render(request, "user_templates/add_booking.html", {"booking_form": booking_form})


@login_required(login_url='/login_form')
def update_booking(request, update_id):
    """
    Called when user want to update any particular booking
    :param request:
    :param update_id:
    :return:
    """
    booking_tobe_updated = get_object_or_404(Booking, pk=update_id)
    if request.POST:
        booking_form = BookingForm(request.POST, instance=booking_tobe_updated)
        if booking_form.is_valid():
            for blocked_room in booking_tobe_updated.rooms.all():
                blocked_room.room_status = "Available"
                blocked_room.save()
            booking_tobe_updated.rooms.clear()
            booking_form.save()
            for updated_room in booking_form.cleaned_data['rooms']:
                updated_room.room_status = "NotAvailable"
                updated_room.save()
            return redirect(view_booking)
    else:
        booking_form = BookingForm(instance=booking_tobe_updated)
    return render(request, "user_templates/update_booking.html",
                  {"booking_form": booking_form, "update_id": update_id})


@login_required(login_url='/login_form')
def delete_booking(request, delete_id):
    """
    Called when user want to delete any particular booking
    :param request:
    :param delete_id:
    :return:
    """
    booking_tobe_deleted = get_object_or_404(Booking, pk=delete_id)
    for blocked_room in booking_tobe_deleted.rooms.all():
        blocked_room.room_status = "Available"
        blocked_room.save()
    booking_tobe_deleted.delete()
    return redirect(view_booking)


@login_required(login_url='/login_form')
def view_customer(request):
    """
    Called to view list of customers from database
    :param request:
    :return:
    """
    all_customers = Customer.objects.all()
    my_pagination = Paginator(all_customers, 5)

    page_number = request.GET.get('page', 1)
    page_obj = my_pagination.page(page_number)
    return render(request, "user_templates/my_customers.html", {"page_obj": page_obj})


@login_required(login_url='/login_form')
def add_customer(request):
    """
    Called to add new customer to database
    :param request:
    :return:
    """
    if request.POST:
        customer_form = CustomerForm(request.POST)
        if customer_form.is_valid():
            customer_form.save()
            CustomerForm()
            return redirect(view_customer)
    else:
        customer_form = CustomerForm()
    return render(request, "user_templates/add_customer.html", {"customer_form": customer_form})


@login_required(login_url='/login_form')
def update_customer(request, update_id):
    """
    Called to update specific customer
    :param request:
    :param update_id:
    :return:
    """
    customer_tobe_updated = get_object_or_404(Customer, pk=update_id)
    if request.POST:
        customer_form = CustomerForm(request.POST, instance=customer_tobe_updated)
        if customer_form.is_valid():
            customer_form.save()
            return redirect(view_customer)
    else:
        customer_form = CustomerForm(instance=customer_tobe_updated)
    return render(request, "user_templates/update_customer.html",
                  {"customer_form": customer_form, "update_id": update_id})


@login_required(login_url='/login_form')
def delete_customer(request, delete_id):
    """
    Called to delete any customer
    :param request:
    :param delete_id:
    :return:
    """
    customer_tobe_deleted = get_object_or_404(Customer, pk=delete_id)

    if customer_tobe_deleted.booking_set.all():
        print("You can not delete Customer because it used in booking")
    else:
        customer_tobe_deleted.delete()
    return redirect(view_customer)
