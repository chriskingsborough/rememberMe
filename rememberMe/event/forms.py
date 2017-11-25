from django.forms import ModelForm
from django import forms
from index.models import User
from event.models import Event

class DateInput(forms.DateInput):
    input_type = 'date'

class EventForm(ModelForm):
    class Meta:
        model = Event
        fields = [
            'event_name',
            'message',
            'start_date',
            'end_date',
            'recurring',
            'interval',
            'interval_type',
            'warning',
            'warning_interval',
            'warning_interval_type',
            'notification_method'
        ]

        widgets = {
            'event_name': forms.TextInput(),
            'recurring': forms.CheckboxInput(),
            'message': forms.Textarea(),
            'start_date': DateInput(),
            'end_date': DateInput(),
            'interval': forms.NumberInput(),
            'warning': forms.CheckboxInput(),
            'warning_interval': forms.NumberInput(),
        }

