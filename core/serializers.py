from rest_framework import serializers
from .models import Dueno, Mascota

class DuenoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dueno
        fields = '__all__'

class MascotaSerializer(serializers.ModelSerializer):
    dueno_nombre = serializers.ReadOnlyField(source='dueno.nombre')

    class Meta:
        model = Mascota
        fields = '__all__'