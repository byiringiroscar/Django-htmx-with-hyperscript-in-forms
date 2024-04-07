from django import forms


class EventUserForm(forms.Form):
    name = forms.CharField(max_length=100)


    def __init__(self, *args, **kwargs):
        if 'event' in kwargs:  # we added this to pass the event to the form when it is created in the view
            self.event = kwargs.pop('event')
        
        super().__init__(*args, **kwargs)

    
    def clean(self):
        # cleaned_data = super().clean()
        if self.event.users.count() >= self.event.number_of_places:
            raise forms.ValidationError('No places left at this event')
        return super().clean()
       