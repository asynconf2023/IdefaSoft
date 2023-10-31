from django.forms import modelform_factory
from django.http import HttpRequest, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.apps import apps

from .forms import InterestRateForm
from .models import Kilometers, Years, Passengers, InterestRate, VehicleType, Energy


def home(request: HttpRequest):
    if request.method == "POST":
        form = InterestRateForm(request.POST)
        if form.is_valid():
            kilometer_value = form.cleaned_data.get('kilometer')
            year_value = form.cleaned_data.get('year')
            vehicle_note = form.cleaned_data.get('vehicle_type').note
            energy_note = form.cleaned_data.get('energy').note
            kilometer_note = Kilometers.objects.get(start__lte=kilometer_value, end__gt=kilometer_value).note
            year_note = Years.objects.get(start__lte=year_value, end__gt=year_value).note
            passenger_percentage = Passengers.objects.get(number=form.cleaned_data.get('passager_number')).percentage
            vehicle_score = round(vehicle_note + energy_note + kilometer_note + year_note)
            interest_rate = InterestRate.objects.get(start__lte=vehicle_score, end__gt=vehicle_score)
            if interest_rate:
                return render(request, 'footprint.html', {
                    'vehicle_note': vehicle_note,
                    'energy_note': energy_note,
                    'kilometer_note': kilometer_note,
                    'year_note': year_note,
                    'vehicle_score': vehicle_score,
                    'passenger_percentage': passenger_percentage,
                    'interest_rate': interest_rate.percentage + passenger_percentage,
                    'form': form,
                })
            else:
                print("ERROR")

    form = InterestRateForm()
    return render(request, 'footprint.html', {'form': form, 'interest_rate': False})


def list_models_by_category(request):
    models = [
        VehicleType,
        Energy,
        Kilometers,
        Years,
        InterestRate,
        Passengers,
    ]
    models_by_category = {}
    name_to_verbose_name = {}
    for model in models:
        category = model.__name__.lower()
        models_by_category[category] = []
        name_to_verbose_name[category] = model._meta.verbose_name
        models_by_category[category].extend([x for x in model.objects.all()])
    context = {
        "models_by_category": models_by_category,
        "name_to_verbose_name": name_to_verbose_name
    }
    return render(request, "list_models_by_category.html", context)


def add_model(request, category):
    model = apps.get_model(app_label='EcoFootprintCalc', model_name=category)
    form_class = modelform_factory(model, fields='__all__')
    form = form_class(request.POST or None)
    if form.is_valid():
        model = form.save(commit=False)
        model.category = category
        model.save()
        return HttpResponseRedirect(reverse("list"))

    context = {
        "form": form,
        "category": category,
    }
    return render(request, "add_model.html", context)
