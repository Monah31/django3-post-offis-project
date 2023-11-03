from rest_framework import generics, viewsets
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from django.forms import model_to_dict

from .models import Letters
from .serializers import LettersSerializer


class LettersViewSet(viewsets.ModelViewSet):
    queryset = Letters.objects.all()
    serializer_class = LettersSerializer


