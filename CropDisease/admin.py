from django.contrib import admin
from .models import CropDisease
# Register your models here.

class CropDiseaseAdmin(admin.ModelAdmin):
    list_display = ['cropname',]

admin.site.register(CropDisease, CropDiseaseAdmin)
