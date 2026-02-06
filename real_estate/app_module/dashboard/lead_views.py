from django.shortcuts import render, redirect
from .forms import LeadForm


def add_lead_view(request):
    if request.method == 'POST':
        form = LeadForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('add_lead')
    else:
        form = LeadForm()

    return render(request, 'add_lead.html', {'form': form})
