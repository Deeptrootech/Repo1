"""admins_work URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from . import views

urlpatterns = [
    path('', views.user_index, name='user_index'),

    path('bookings/', views.view_booking, name='view_booking'),
    path('add_booking/', views.add_booking, name='add_booking'),
    path('update_booking/<int:update_id>/', views.update_booking, name='update_booking'),
    path('delete_booking/<int:delete_id>/', views.delete_booking, name='delete_booking'),

    path('rooms/', views.view_rooms, name='view_rooms'),
    path('add_rooms/', views.add_rooms, name='add_rooms'),
    path('update_room/<int:update_id>/', views.update_rooms, name='update_room'),
    path('delete_room/<int:delete_id>/', views.delete_rooms, name='delete_room'),

    path('extra_services/', views.view_extra_services, name='view_extra_services'),
    path('add_extra_services/', views.add_extra_services, name='add_extra_services'),
    path('update_extra_services/<int:update_id>/', views.update_extra_services,
         name='update_extra_services'),
    path('delete_extra_services/<int:delete_id>/', views.delete_extra_services,
         name='delete_extra_services'),

    path('customer/', views.view_customer, name='view_customer'),
    path('add_customer/', views.add_customer, name='add_customer'),
    path('update_customer/<int:update_id>/', views.update_customer, name='update_customer'),
    path('delete_customer/<int:delete_id>/', views.delete_customer, name='delete_customer'),

]

urlpatterns += static(settings.MEDIA_URL,
                      document_root=settings.MEDIA_ROOT)
