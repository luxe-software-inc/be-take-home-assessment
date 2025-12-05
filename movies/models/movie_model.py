from django.db import models
from movies.models.base_model import BaseModel


class MovieModel(BaseModel):

    id = models.AutoField(
        verbose_name='Movie ID',
        primary_key=True
    )

    title = models.CharField(
        verbose_name='Title',
        max_length=255,
    )

    release_date = models.DateField(
        verbose_name='Release Date',
        null=True,
        blank=True,
    )

    genres = models.JSONField(
        verbose_name='Genres',
        default=list,
        blank=True,
    )

    director = models.CharField(
        verbose_name='Director',
        max_length=255,
        blank=True,
    )

    cast = models.JSONField(
        verbose_name='Cast',
        default=list,
        blank=True,
    )

    description = models.TextField(
        verbose_name='Description',
        blank=True,
    )

    rating = models.DecimalField(
        verbose_name='Rating',
        max_digits=3,
        decimal_places=1,
        null=True,
        blank=True,
    )

    duration_minutes = models.IntegerField(
        verbose_name='Duration (minutes)',
        null=True,
        blank=True,
    )

    poster_url = models.URLField(
        verbose_name='Poster URL',
        max_length=500,
        blank=True,
    )

    def __str__(self):
        return f"{self.title} ({self.release_date})" if self.release_date else self.title

    class Meta:
        verbose_name = 'Movie'
        verbose_name_plural = 'Movies'
