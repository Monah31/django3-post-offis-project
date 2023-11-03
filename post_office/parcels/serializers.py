from rest_framework import serializers
from .models import Parcels
from rest_framework.renderers import JSONRenderer

class ParcelsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Parcels
        fields = "__all__"
