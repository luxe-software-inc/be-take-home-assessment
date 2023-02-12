from django.db import models
from movies.models.base_model import BaseModel


class WishlistModel(BaseModel):

    id = models.AutoField(
        verbose_name='Wishlist Item ID',
        primary_key=True
    )

    # TASK --> Add more fields here
