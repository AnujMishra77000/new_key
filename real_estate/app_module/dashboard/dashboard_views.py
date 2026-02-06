from django.shortcuts import render, redirect
from app_module.models import Flat, ResaleFlat, RentFlat
from .forms import FlatForm, RentFlatForm, ResaleFlatForm


def add_flat_view(request):
    if request.method == 'POST':
        form = FlatForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('add_flat')  # stay on same page

    else:
        form = FlatForm()

    return render(request, 'add_flat.html', {'form': form})

def add_resale_flat(request):
    form = ResaleFlatForm(request.POST or None, request.FILES or None)

    if form.is_valid():
        form.save()
        return redirect('add_resale')

    return render(request, 'add_resale.html', {'form': form})

def add_rent_flat(request):
    form = RentFlatForm(request.POST or None, request.FILES or None)

    if form.is_valid():
        form.save()
        return redirect('add_rent')

    return render(request, 'add_rent.html', {'form': form})

