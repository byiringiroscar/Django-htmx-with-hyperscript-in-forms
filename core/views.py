from django.shortcuts import render
from core.models import Event, EventUser
from core.forms import EventUserForm

# Create your views here.


def index(request):
    event = Event.objects.get_or_create(name='Primavera Sound', number_of_places=3)[0]
    context = {
        'event': event,
        'form': EventUserForm()
    }
    return render(request, 'index.html')