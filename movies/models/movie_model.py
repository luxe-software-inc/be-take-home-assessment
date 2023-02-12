from django.db import models
from movies.models.base_model import BaseModel


class MovieModel(BaseModel):

    id = models.AutoField(
        verbose_name='Movie ID',
        primary_key=True
    )

    # TASK --> Add more fields here
