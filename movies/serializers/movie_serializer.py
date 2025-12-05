from rest_framework import serializers
from movies.models.movie_model import MovieModel


class MovieSerializer(serializers.ModelSerializer):

    class Meta:
        model = MovieModel
        fields = [
            'id', 'title', 'release_date', 'genres', 'director', 'cast',
            'description', 'rating', 'duration_minutes', 'poster_url'
        ]
        read_only_fields = ['id']
