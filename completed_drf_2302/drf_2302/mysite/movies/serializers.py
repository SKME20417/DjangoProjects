from .models import Moviedata
from rest_framework import serializers


class MovieSerializer(serializers.ModelSerializer):
    image = serializers.ImageField(max_length=None, use_url = True)
    class Meta:
        model = Moviedata
        fields = ['id', 'title', 'year', 'duration', 'rating', 'genre', 'image']
        
        