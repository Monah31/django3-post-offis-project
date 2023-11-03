from django.shortcuts import render
from rest_framework import generics, viewsets
from .models import Parcels
from .serializers import ParcelsSerializer


class ParcelsViewSet(viewsets.ModelViewSet):
    queryset = Parcels.objects.all()
    serializer_class = ParcelsSerializer