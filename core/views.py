from django.shortcuts import render
from core.models import Event, EventUser
from core.forms import EventUserForm

# Create your views here.


def index(request):
    event = Event.objects.get_or_create(name='Primavera Sound', number_of_places=3)[0]
    if request.method == 'POST':
        form = EventUserForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            EventUser.objects.create(name=name, event=event)
            context = {
                'users': event.users.all()
            }
            return render(request, 'partials/userlist.html', context)
    context = {
        'event': event,
        'form': EventUserForm(),
        'users': event.users.all()
    }
    return render(request, 'index.html', context)