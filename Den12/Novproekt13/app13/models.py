from django.db import models

# Create your models here.
class Zemji(models.Model):
    country = models.CharField(max_length=50, unique=True)  #String
    population = models.IntegerField()
    year_change = models.FloatField()  #decimali
    net_change = models.IntegerField()
    density = models.IntegerField()
    land_area = models.IntegerField()
    med_age = models.IntegerField()
    urban_pop = models.IntegerField()
    world_share = models.FloatField()  #decimali

