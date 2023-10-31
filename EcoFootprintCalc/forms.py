from django import forms
from django.db.models import Min, Max
from django.forms import ModelForm

from .models import VehicleType, Energy, Kilometers, Years, Passengers


class InterestRateForm(forms.Form):
    vehicle_type = forms.ModelChoiceField(queryset=VehicleType.objects.all(),
                                          label="Type de véhicule",
                                          widget=forms.Select(attrs={'class': 'input'}),
                                          initial=VehicleType.objects.first()
                                          )
    energy = forms.ModelChoiceField(queryset=Energy.objects.all(),
                                    label="Energie",
                                    widget=forms.Select(attrs={'class': 'input'}),
                                    initial=Energy.objects.first()
                                    )
    kilometer = forms.IntegerField(min_value=Kilometers.objects.aggregate(Min('start'))['start__min'],
                                   max_value=Kilometers.objects.aggregate(Max('end'))['end__max'],
                                   label="Kilomètres parcourus par an (en milliers)",
                                   widget=forms.NumberInput(attrs={'placeholder': '25', 'class': 'input'})
                                   )
    year = forms.IntegerField(min_value=Years.objects.aggregate(Min('start'))['start__min'],
                              max_value=Years.objects.aggregate(Max('end'))['end__max'],
                              label="Année du véhicule",
                              widget=forms.NumberInput(attrs={'placeholder': '2009', 'class': 'input'})
                              )
    passager_number = forms.IntegerField(min_value=Passengers.objects.aggregate(Min('number'))['number__min'],
                                         max_value=Passengers.objects.aggregate(Max('number'))['number__max'],
                                         label="Nombre de passagers",
                                         widget=forms.NumberInput(attrs={'placeholder': '1', 'class': 'input'})
                                         )
