from django.contrib import admin
from .models import Activiteit

@admin.register(Activiteit)
class ActiviteitAdmin(admin.ModelAdmin):
    pass