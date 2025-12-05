from django.db import models

from movies.models.base_model import BaseModel
from movies.models.customer_model import CustomerModel
from movies.models.movie_model import MovieModel


class WishlistModel(BaseModel):

    id = models.AutoField(
        verbose_name='Wishlist Item ID',
        primary_key=True
    )

    customer = models.ForeignKey(
        CustomerModel,
        verbose_name='Customer',
        on_delete=models.CASCADE,
        related_name='wishlists',
    )

    movie = models.ForeignKey(
        MovieModel,
        verbose_name='Movie',
        on_delete=models.CASCADE,
        related_name='wishlists',
    )

    def __str__(self):
        return f"{self.customer} - {self.movie}"

    class Meta:
        verbose_name = 'Wishlist Item'
        verbose_name_plural = 'Wishlist Items'
        unique_together = ['customer', 'movie']
