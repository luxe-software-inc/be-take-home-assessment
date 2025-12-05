from rest_framework import status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from movies.models.wishlist_model import WishlistModel
from movies.serializers.wishlist_serializer import WishlistSerializer
from movies.serializers.movie_serializer import MovieSerializer


class WishlistViewSet(ModelViewSet):
    serializer_class = WishlistSerializer
    queryset = WishlistModel.objects.all()

    @action(
        detail=False,
        methods=['get'],
        url_path='all_movies/(?P<customer_id>[^/.]+)',
    )
    def all_movies(self, request, customer_id=None):
        wishlists = WishlistModel.objects.filter(
            customer_id=customer_id
        ).select_related('movie')
        movies = [wishlist.movie for wishlist in wishlists]
        serializer = MovieSerializer(movies, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
