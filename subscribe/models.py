from django.db import models
from .get_all_countries import ALL_COUNTRIES


# Create your models here.
class Subscribe(models.Model):
    name = models.CharField(max_length=50, null=True, blank=False)
    email = models.EmailField(max_length=100, null=True, unique=True)
    country = models.CharField(choices=ALL_COUNTRIES, max_length=100, null=True)
