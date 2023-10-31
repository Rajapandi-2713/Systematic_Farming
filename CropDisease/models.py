from django.db import models

# Create your models here.
class CropDisease(models.Model):
    cropname = models.CharField(max_length=50)
    diseasename = models.CharField(max_length=100)
    description = models.TextField()
    diseaseimage = models.ImageField(upload_to = 'static/images/disease/')
    identification = models.TextField()
    prevention = models.TextField()
    treatment = models.TextField()
