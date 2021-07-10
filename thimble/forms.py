from django import forms
from .models import Thimble, City, Country


class ThimbleForm(forms.ModelForm):
    class Meta:
        model = Thimble
        fields = ('number', 'country', 'city', 'matherial', 'type', 'description', 'image')

class Search(forms.Form):
    search = forms.CharField(required=False, label="")

class CountryForm(forms.ModelForm):
    class Meta:
        model = Country
        fields = ('name', 'region')

class CityForm(forms.ModelForm):
    class Meta:
        model = City
        fields = ('name', 'region', 'country')