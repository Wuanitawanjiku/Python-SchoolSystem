from django import forms
from.models import Events
from django.forms import fields

class EventRegistrationForm(forms.ModelForm):
    class Meta:
        model =Events
        fields="__all__"