from rest_framework import serializers
from movies.models.wishlist_model import WishlistModel


class WishlistSerializer(serializers.ModelSerializer):

    class Meta:
        model = WishlistModel
        fields = ['id', 'customer', 'movie']
        read_only_fields = ['id']
