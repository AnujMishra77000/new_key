from rest_framework import generics, filters
from app_module.models import Flat, Builder
from django_filters.rest_framework import DjangoFilterBackend
from app_module.models import (Flat, 
                               Builder, 
                               Campaign, 
                               Category,
                               Lead,
                               ResaleFlat, 
                               RentFlat)
from .serializers import (FlatSerializer, 
                          BuilderSerializer, 
                          LeadSerializer, 
                          CategorySerializer,
                          ResaleFlatSerializer,
                          RentFlatSerializer
)

# it gives list of builder with us
class BuilderListView(generics.ListAPIView):
    queryset = Builder.objects.all()
    serializer_class = BuilderSerializer

class CategoryViews(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


# This can handle Builder section default flats, category click, latest flat, future search/filter

class FlatListView(generics.ListAPIView):
    queryset = Flat.objects.all().order_by('-created_at') 
    serializer_class = FlatSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]    
    filterset_fields = ['builder', 'category']
    search_fields = ['title', 'description']

# flat details for whatsapp autofill
class FlatDetailView(generics.RetrieveAPIView):
    queryset = Flat.objects.all()
    serializer_class = FlatSerializer        


class ResaleFlatListView(generics.ListAPIView):
    queryset = ResaleFlat.objects.all().order_by('-created_at')
    serializer_class = ResaleFlatSerializer
    filterset_fields = ['category']


class RentFlatListView(generics.ListAPIView):
    queryset = RentFlat.objects.all().order_by('-created_at')
    serializer_class = RentFlatSerializer
    filterset_fields = ['category']
