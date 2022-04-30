from django.shortcuts import render
from .models import Zemji
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import CountriesSerializers
# Create your views here.

@api_view(['GET'])
def get_all_countries(request):
    all_countries = Zemji.objects.all()
    countries_serializer = CountriesSerializers(all_countries, many = True)
    return Response(countries_serializer.data)

# API end point za samo edna drzava koja ke se kaze od get promenliva
@api_view(['GET'])
def get_all_countries(request):
    one_country = Zemji.objects.get()
    countries_serializer = CountriesSerializers(one_country)
    return Response(countries_serializer.data)

# API endpoint za site drzavi koi imaat pomalo naselenie od odredena brojka koja ke se kaze od get promenliva
@api_view(['GET'])
def get_all_countries(request):
    lower_countries = Zemji.objects.filter()
    countries_serializer = CountriesSerializers(lower_countries)
    return Response(countries_serializer.data)

# API endpoint za site drzavi kade ke se prikazuvaat po azbucen redosled, opcionalno dodadete korisnikot da moze\
# da moze da bira dali od pocetok ili od kraj

@api_view(['GET'])
def get_all_countries(request):
    all_countries = Zemji.objects.all(all_countries, Reverse = True)
    countries_serializer = CountriesSerializers(all_countries)
    return Response(countries_serializer.data)

@api_view(['GET'])
def matematicki_operacii(request):
    broj1 = request.GET["broj1"]
    broj2 = request.GET["broj2"]
    zbir = int(broj1) + int(broj2)
    broj3 = request.GET["broj3"]
    broj4 = request.GET["broj4"]
    razlika = int(broj3) - int(broj4)
    broj5 = request.GET["broj5"]
    broj6 = request.GET["broj6"]
    proizvod = int(broj5) * int(broj6)
    broj7 = request.GET["broj7"]
    broj8 = request.GET["broj8"]
    kolicnik = int(broj7) / int(broj8)
    data = {'zbir': zbir, 'razlika': razlika, 'proizvod': proizvod, 'kolicnik': kolicnik}

    return Response(data)
















