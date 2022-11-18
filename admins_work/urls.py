from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from . import views

urlpatterns = [
    path('', views.user_index, name='user_index'),

    path('add_booking/', views.make_booking, name='make_booking'),

    path('rooms/', views.view_rooms, name='view_rooms'),
    path('add_rooms/', views.add_rooms, name='add_rooms'),
    path('update_room/<int:update_id>/', views.update_customer, name='update_customer'),
    path('delete_room/<int:delete_id>/', views.delete_customer, name='delete_customer'),

    path('extra_services/', views.view_extra_services, name='view_extra_services'),
    path('add_extra_services/', views.add_extra_services, name='add_extra_services'),

    path('customer/', views.view_customer, name='view_customer'),
    path('add_customer/', views.add_customer, name='add_customer'),
    path('update_customer/<int:update_id>/', views.update_customer, name='update_customer'),
    path('delete_customer/<int:delete_id>/', views.delete_customer, name='delete_customer'),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
