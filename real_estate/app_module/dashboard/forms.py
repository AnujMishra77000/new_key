from django import forms
from ..models import Flat, Lead, RentFlat, ResaleFlat


class FlatForm(forms.ModelForm):
    class Meta:
        model = Flat
        fields = [
            'builder',
            'category',
            'title',
            'description',
            'price',
            'image',
            'blueprint',
        ]

class LeadForm(forms.ModelForm):
    class Meta:
        model = Lead
        fields = '__all__'
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Customer name'}),
            'phone': forms.TextInput(attrs={'placeholder': 'Phone number'}),
        }

class ResaleFlatForm(forms.ModelForm):
    class Meta:
        model = ResaleFlat
        fields = [
            'title',
            'description',
            'price',
            'category',
            'image',
            'blueprint',
        ]

class RentFlatForm(forms.ModelForm):
    class Meta:
        model = RentFlat
        fields = [
            'title',
            'description',
            'monthly_price',
            'category',
            'image',
            'blueprint',
        ]