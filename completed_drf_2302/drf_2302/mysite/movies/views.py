from django.shortcuts import render
from .models import Moviedata
from .serializers import MovieSerializer
from rest_framework import viewsets

# Create your views here.

class MovieViewSet(viewsets.ModelViewSet):
    queryset = Moviedata.objects.all()
    serializer_class = MovieSerializer
    
class ActionViewSet(viewsets.ModelViewSet):
    queryset = Moviedata.objects.filter(genre = "action")
    serializer_class = MovieSerializer
    
class ComedyViewSet(viewsets.ModelViewSet):
    queryset = Moviedata.objects.filter(genre = "comedy")
    serializer_class = MovieSerializer
    
    
    
    
    