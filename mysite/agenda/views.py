from django.shortcuts import render
from .models import Activiteit

def agenda(request):
    activiteiten = Activiteit.objects.all()
    return render(request, 'agenda/agenda.html', {'activiteiten': activiteiten})