from django import forms


class EventUserForm(forms.Form):
    name = forms.CharField(max_length=100)