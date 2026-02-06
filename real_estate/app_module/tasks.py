from celery import shared_task
from app_module.models import Lead, Campaign
from django.core.mail import send_mail
from django.conf import settings
from django.utils import timezone

@shared_task(bind=True)
def run_campaign(self, campaign_id):
    campaign = Campaign.objects.get(id=campaign_id)

    # prevent re-running
    if campaign.status == 'COMPLETED':
        print(f"Campaign {campaign.id} already completed. Skipping.")
        return

    campaign.status = 'RUNNING'
    campaign.save()

    leads = Lead.objects.exclude(email__isnull=True)
    campaign.total_leads = leads.count()
    campaign.save()

    for lead in leads:
        try:
            send_mail(
                subject="New Real Estate Offer",
                message=campaign.message,
                from_email=settings.EMAIL_HOST_USER,
                recipient_list=[lead.email],
            )
            campaign.sent_count += 1
        except Exception as e:
            print(f"Failed sending to {lead.email}: {e}")
            campaign.failed_count += 1
        campaign.save()

    campaign.status = 'COMPLETED'
    campaign.executed_at = timezone.now()
    campaign.save()
    print(f"Campaign {campaign.id} completed.")


@shared_task
def check_and_run_campaigns():
    now = timezone.now()
    campaigns = Campaign.objects.filter(
        scheduled_time__lte=now,
        status='SCHEDULED'
    )
    for campaign in campaigns:
        run_campaign.delay(campaign.id)
