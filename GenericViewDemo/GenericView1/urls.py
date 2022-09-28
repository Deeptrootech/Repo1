"""GenericViewDemo URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.urls import path

from . import views

urlpatterns = [
    path('', views.StudentCreateView.as_view(), name="StudentCreate"),
    path('list/', views.StudentListView.as_view(), name="StudentList"),
    path('<pk>/', views.StudentDetailView.as_view(), name="StudentDetail"),
    path('<pk>/update', views.StudentUpdateView.as_view(), name="StudentUpdate"),
    path('<pk>/delete/', views.StudentDeleteView.as_view(), name="StudentDelete")
]
