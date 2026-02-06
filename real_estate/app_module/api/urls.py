from django.urls import path
from .views import (
    BuilderListView,
    CategoryViews,
    FlatListView,
    FlatDetailView,
   ResaleFlatListView,
   RentFlatListView   
)

urlpatterns = [
    path('builders/', BuilderListView.as_view()),
    path('categories/', CategoryViews.as_view()),
    path('flats/', FlatListView.as_view()),
    path('flats/<int:pk>/', FlatDetailView.as_view()),
    path('resale/',ResaleFlatListView.as_view()),
    path('rent/',RentFlatListView.as_view()),
    
]
