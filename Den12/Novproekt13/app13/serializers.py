from rest_framework import serializers
from .models import Zemji

class CountriesSerializers(serializers.ModelSerializer):

    class Meta:
        model = Zemji
        fields = '__all__'