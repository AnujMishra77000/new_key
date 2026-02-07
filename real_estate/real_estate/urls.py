"""
URL configuration for real_estate project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from app_module.views import home, flats, rental, resale

urlpatterns = [
    path('admin/', admin.site.urls),
    
    path('', home),
    path('flats/', flats),
    path('rental/', rental),
    path('resale/', resale),
    
    path('api/', include('app_module.api.urls')),
    path('dash/', include('app_module.dashboard.urls')),
    
    

]

urlpatterns +=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)