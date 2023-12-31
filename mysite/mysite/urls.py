from django.contrib import admin
from django.urls import path, include
from agenda.views import agenda

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('agenda.urls')),
]