from django.urls import path
from .dashboard_views import add_flat_view
from app_module.campaign_views import add_campaign_view, campaign_tracker
from .dashboard_views import add_rent_flat,add_resale_flat 
from .lead_views import  add_lead_view
from .homes import dashboard_home

urlpatterns = [
    path('',dashboard_home,name='dashboard_home'),
    path('add-flat/', add_flat_view, name='add_flat'),
    path('add-campaign/', add_campaign_view, name='add_campaign'),
    path('add-lead/', add_lead_view, name='add_lead'),
    path('campaign-tracker/', campaign_tracker, name='campaign_tracker'),
    path('add_resale/',add_resale_flat , name='add_resale'),
    path('add_rent/',add_rent_flat , name='add_rent'),

    
]
