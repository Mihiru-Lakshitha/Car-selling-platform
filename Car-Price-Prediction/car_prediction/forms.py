from django import forms
from .models import CarInput

class CarInputForm(forms.ModelForm):
    class Meta:
        model = CarInput
        fields = ['mileage', 'num_owners', 'year', 'starting_bid']

