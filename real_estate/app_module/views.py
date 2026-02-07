from django.shortcuts import render


def home(request):
    return render(request, 'website/index.html')

def flats(request):
    return render(request, 'website/flats.html')

def rental(request):
    return render(request, 'website/rental_api.html')

def resale(request):
    return render(request, 'website/resale_api.html')
