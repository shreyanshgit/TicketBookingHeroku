from django.shortcuts import render
from rest_framework import viewsets
from .models import Hero
from .serializers import HeroSerializers

# Create your views here.
class HeroViewSet(viewsets.ModelViewSet):
    queryset = Hero.objects.all().order_by('alias')
    serializer_class = HeroSerializers