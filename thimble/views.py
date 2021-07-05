from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse

from .forms import ThimbleForm, Search, CountryForm, CityForm
from .models import Thimble, Country, City

def edit_thimble(request, thimble_id=None):
    thimble = None
    if thimble_id:
        thimble = Thimble.objects.get(id=thimble_id)
    form = ThimbleForm(request.POST or None, files=request.FILES or None, instance=thimble)
    if form.is_valid():
        form.save()
        return redirect('edit_thimble', thimble_id=form.instance.id)
    # TODO errors when
    return render(request, 'thimble/edit.html', context={
            'form': form,
        })

def create_countries(request, country_id=None):
    country = None
    if country_id:
        country = Country.objects.get(id=country_id)
    form = CountryForm(request.POST or None, instance=country)
    if form.is_valid():
        form.save()
    # TODO errors when
    return render(request, 'thimble/edit_country.html', context={
        'form': form,
    })

def create_city(request, city_id=None):
    city = None
    if city_id:
        city = City.objects.get(id=city_id)
    form = CityForm(request.POST or None, instance=city)
    if form.is_valid():
        form.save()
    # TODO errors when
    return render(request, 'thimble/edit_city.html', context={
        'form': form,
    })

def thimbles(request):
    form = Search(request.GET or None)
    thimbles = Thimble.objects.all()
    if form.is_valid():
        thimbles = Thimble.objects.filter(city__istartswith=form.cleaned_data['search'])
    context = {
        'thimbles': thimbles,
        'form': form
    }
    return render(request, 'thimble/thimbles.html', context)

def main(request):
    return render(request, 'thimble/main.html')


def key_sort(arg):
    name = arg.name
    if name.isdigit():
        res = int(name)
    else:
        res = name
    return res


def russia(request):
    cities = sorted(City.objects.filter(country__name="Россия"), key=key_sort)
    regions = {}
    for c in cities:
        regions.setdefault(c.region, []).append(c)
    context = {
        'cities': cities,
        'regions': regions
    }
    return render(request, 'thimble/russia.html', context)

def countries(request):
    countries = sorted(Country.objects.all(), key=key_sort)
    regions = {}
    for c in countries:
        regions.setdefault(c.region, []).append(c)
    context = {
        'countries': countries,
        'regions': regions
    }
    return render(request, 'thimble/countries.html', context)

def souvenir(request):
    form = Search(request.GET or None)
    thimbles = Thimble.objects.filter(type="Сувенирный")
    if form.is_valid():
        thimbles = Thimble.objects.filter(city__istartswith=form.cleaned_data['search'], type="Сувенирный")
    context = {
        'thimbles': thimbles,
        'form': form,
    }
    return render(request, 'thimble/souvenir.html', context)

def classic(request):
    form = Search(request.GET or None)
    thimbles = Thimble.objects.filter(type="Рабочий")
    if form.is_valid():
        thimbles = Thimble.objects.filter(city__istartswith=form.cleaned_data['search'], type="Рабочий")
    context = {
        'thimbles': thimbles,
        'form': form,
    }
    return render(request, 'thimble/classic.html', context)



def thimbles_info(request, thimble_id):
   context = {
       'thimbles_info': Thimble.objects.get(id=thimble_id)
   }
   return render(request, 'thimble/thimbles_info.html', context)

def country_info(request, country_id):
    country_name = Country.objects.get(id=country_id).name
    thimbles = Thimble.objects.filter(country__name=country_name)
    context = {
        'country_info': Country.objects.get(id=country_id),
        'thimbles': thimbles,
    }
    return render(request, 'thimble/country_info.html', context)

def city_info(request, city_id):
    thimbles = Thimble.objects.filter(country__name="Россия")
    context = {
        'city_info': City.objects.get(id=city_id),
        'thimbles': thimbles,
    }
    return render(request, 'thimble/city_info.html', context)

def del_thimbles(request, thimble_id):
    b = Thimble.objects.get(id=thimble_id)
    b.delete()
    return redirect(reverse('thimbles'))