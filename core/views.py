from django.shortcuts import render
from core.models import Event, EventUser
from core.forms import EventUserForm
import time
from django.http import JsonResponse

# Create your views here.


def index(request):
    event = Event.objects.get_or_create(name='Primavera Sound', number_of_places=3)[0]
    if request.method == 'POST':
        time.sleep(1)  # we added this for testing to check if hyperscript will disable the button after form submitted with htmx
        form = EventUserForm(request.POST, event=event)
        if form.is_valid():
            name = form.cleaned_data['name']
            EventUser.objects.create(name=name, event=event)
            context = {
                'users': event.users.all()
            }
            return render(request, 'partials/userlist.html', context)
        
        context = {'form': form}
        response = render(request, 'partials/form.html', context)
        response['HX-Retarget'] = '#submit-form' # we added this to retarget the form after submission with htmx
        return response
    context = {
        'event': event,
        'form': EventUserForm(),
        'users': event.users.all()
    }
    return render(request, 'index.html', context)


def check_spaces(request):
    # event = Event.objects.get(name='Primavera Sound')
    event = Event.objects.first()
    spaces_available = event.users.count() < event.number_of_places
    return JsonResponse({'available': spaces_available})