from rest_framework import serializers
from apirest.models import Sensores, Lecturas, Pruebas

class SensoresSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Sensores
        fields = ('id', 'temperatura', 'peso', 'humedad',)

class LecturasSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lecturas
        fields = ('id', 'key', 'value','data_created',)

class PruebasSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pruebas
        fields = ('id', 'nombre', 'edad', 'direccion',)
