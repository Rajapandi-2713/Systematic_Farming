from unittest.util import _MAX_LENGTH
from django.db import models

# Create your models here.

class CropCultivation(models.Model):
    name = models.CharField(max_length=50)
    intro = models.TextField(null=True)
    climate_soil = models.TextField()
    landpreparation = models.TextField()
    varieties = models.TextField()
    season_sowing = models.TextField()
    irrigation = models.TextField()
    interculture = models.TextField()
    harvesting = models.TextField()
    cropimage = models.ImageField(upload_to = 'static/images/cultivation/')