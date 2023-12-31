# agenda/urls.py
from django.urls import path
from .views import agenda

urlpatterns = [
    path('', agenda, name='agenda'),
]