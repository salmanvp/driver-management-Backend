from rest_framework import serializers
from . models import Vehcles
from . models import Driver

class Vehcleserializers(serializers.ModelSerializer):
    class Meta:
        model=Vehcles
        fields='__all__'

class Driveserializers(serializers.ModelSerializer):
    class Meta:
        model=Driver
        fields='__all__'