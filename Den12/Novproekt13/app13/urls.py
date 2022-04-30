from django.urls import path
from .views import get_all_countries, matematicki_operacii, operacii

urlpatterns = [
    path("site/", get_all_countries),
    path("matematicki_operacii/", matematicki_operacii),
    path("operacii/", operacii),
    
]


 