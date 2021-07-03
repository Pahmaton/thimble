from django import forms
from .models import Thimble


class ThimbleForm(forms.ModelForm):
    class Meta:
        model = Thimble
        fields = ('number', 'country', 'city', 'matherial', 'description', 'seria', 'stellaj', 'shelf', 'where',
                  'who_present', 'date', 'type', 'image')

class Search(forms.Form):
    search = forms.CharField(required=False, label="")