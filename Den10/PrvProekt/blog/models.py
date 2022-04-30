from django.db import models

# Create your models here.

class Knigi(models.Model):
    naslov = models.CharField(max_length=50, unique=True)
    avtor = models.CharField(max_length=50)
    zanr = models.CharField(max_length=50)
    kolicina = models.IntegerField()
    GodinaIzdavanje = models.IntegerField()
    

class Clen(models.Model):
    ime = models.CharField(max_length=50)
    prezime = models.CharField(max_length=50)
    grad = models.CharField(max_length=50)
    adresa = models.CharField(max_length=50)
    dataRagjanje = models.DateField()
    telefonskibroj = models.CharField(max_length=50)
    clenski_broj = models.IntegerField()
    dataClenstvo = models.DateField()
    pozajmenoKniga = models.BooleanField()
    