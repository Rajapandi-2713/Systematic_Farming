from django.contrib import admin
from .models import CropCultivation
# Register your models here.

class CropCultivationAdmin(admin.ModelAdmin):
    list_display = ['name',]

admin.site.register(CropCultivation, CropCultivationAdmin)

