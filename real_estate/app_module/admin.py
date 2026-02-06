from django.contrib import admin
from .models import Builder, Category, Campaign, Flat, Lead,ResaleFlat,RentFlat
admin.site.register(Builder)
admin.site.register(Category)
admin.site.register(Flat)
admin.site.register(Lead)
admin.site.register(Campaign)
admin.site.register(ResaleFlat)
admin.site.register(RentFlat)
