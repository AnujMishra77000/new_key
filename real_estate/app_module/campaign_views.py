from django.shortcuts import render, redirect
from app_module.models import Campaign
from django.utils import timezone
from datetime import datetime

def add_campaign_view(request):
    if request.method == 'POST':
        message = request.POST.get('message')
        from django.utils import timezone
        dt = datetime.fromisoformat(request.POST.get('scheduled_time'))  # e.g., "2026-02-06T08:55"
        scheduled_time = timezone.make_aware(dt, timezone.get_default_timezone())  # makes aware in Asia/Kolkata

        Campaign.objects.create(
            message=message,
            scheduled_time=scheduled_time
        )

        return redirect('campaign_tracker')

    return render(request, 'add_campaign.html')


def campaign_tracker(request):
    campaigns = Campaign.objects.all().order_by('-created_at')
    return render(request, 'camp_track.html', {'campaigns': campaigns})
