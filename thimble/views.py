from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse

from .forms import ThimbleForm, Search
from .models import Thimble

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

def russia(request):
    # Thimble.objects.filter(country__name="Россия")
    return render(request, 'thimble/russia.html')

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

def del_thimbles(request, thimble_id):
    b = Thimble.objects.get(id=thimble_id)
    b.delete()
    return redirect(reverse('thimbles'))