from django.db import models
from movies.models.base_model import BaseModel


class CustomerModel(BaseModel):
    id = models.AutoField(
        verbose_name='Customer ID',
        primary_key=True
    )
    first_name = models.CharField(
        verbose_name='First Name',
        max_length=100,
    )
    last_name = models.CharField(
        verbose_name='Last Name',
        max_length=100,
    )
    email = models.EmailField(
        verbose_name='Email',
        null=True,

        blank=True,
        unique=True,
    )

    def __str__(self):
        return str(self.first_name) + ' ' + str(self.last_name)
