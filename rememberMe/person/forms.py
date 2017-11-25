from django.forms import ModelForm
from django import forms
from index.models import User
from person.models import Person

class DateInput(forms.DateInput):
    input_type = 'date'

class PersonForm(ModelForm):
    class Meta:
        model = Person
        fields = [
            'name',
            'message',
            'start_date',
            'interval',
            'interval_type',
            'notification_method'
        ]

        widgets = {
            'name': forms.TextInput(),
            'start_date': DateInput(),
            'message': forms.Textarea(),
            'interval': forms.NumberInput(),
        }

