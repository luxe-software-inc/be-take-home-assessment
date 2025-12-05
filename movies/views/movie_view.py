import json
import os
from django.conf import settings
from rest_framework import status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from movies.models.movie_model import MovieModel
from movies.serializers.movie_serializer import MovieSerializer


class MovieViewSet(ModelViewSet):
    serializer_class = MovieSerializer
    queryset = MovieModel.objects.all()

    @action(
        detail=False, methods=['get', 'post'], url_path='load_external_data'
    )
    def load_external_data(self, request):
        """
        Creates new movies and updates existing ones based on title+release_date uniqueness.
        """
        json_file_path = os.path.join(
            settings.BASE_DIR, 'movies', 'data', 'movies_api_response.json'
        )

        try:
            with open(json_file_path, 'r') as file:
                data = json.load(file)
        except FileNotFoundError:
            return Response(
                {'status': 'error', 'message': 'Movies data file not found'},
                status=status.HTTP_404_NOT_FOUND,
            )
        except json.JSONDecodeError:
            return Response(
                {'status': 'error', 'message': 'Invalid JSON format'},
                status=status.HTTP_400_BAD_REQUEST,
            )

        movies_data = data.get('movies', [])
        if not movies_data:
            return Response(
                {
                    'status': 'success',
                    'message': 'No movies to process',
                    'created': 0,
                    'updated': 0,
                },
                status=status.HTTP_200_OK,
            )

        existing_movies = {
            (movie.title, movie.release_date): movie
            for movie in MovieModel.objects.only(
                'id',
                'title',
                'release_date',
                'genres',
                'director',
                'cast',
                'description',
                'rating',
                'duration_minutes',
                'poster_url',
            )
        }

        movies_to_create = []
        movies_to_update = []

        for movie_data in movies_data:
            serializer = MovieSerializer(data=movie_data)
            if not serializer.is_valid():
                continue

            validated = serializer.validated_data
            movie_key = (validated['title'], validated.get('release_date'))

            if movie_key in existing_movies:

                existing_movie = existing_movies[movie_key]
                for field, value in validated.items():
                    setattr(existing_movie, field, value)
                movies_to_update.append(existing_movie)
            else:
                movies_to_create.append(MovieModel(**validated))

        created_movies = MovieModel.objects.bulk_create(movies_to_create)
        updated_count = 0
        if movies_to_update:
            MovieModel.objects.bulk_update(
                movies_to_update,
                [
                    'genres',
                    'director',
                    'cast',
                    'description',
                    'rating',
                    'duration_minutes',
                    'poster_url',
                ],
            )
            updated_count = len(movies_to_update)

        return Response(
            {
                'status': 'success',
                'message': f'Successfully processed {len(movies_data)} movies',
                'created': len(created_movies),
                'updated': updated_count,
            },
            status=status.HTTP_201_CREATED,
        )
