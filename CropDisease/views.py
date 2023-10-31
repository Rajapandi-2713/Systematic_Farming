from django.shortcuts import render,HttpResponse
from .models import CropDisease
# Create your views here.
def diseases(request):
    crop_list = CropDisease.objects.order_by().values('cropname').distinct()
    result = []
    for i in crop_list:
        crop = i['cropname']
        obj = CropDisease.objects.filter(cropname=crop)
        result.append(obj[0])
    my_dict = {'crop_list': result, }
    return render(request, 'CropDisease/cropdiseases.html', context = my_dict)

def cropdiseases(request, name):
    obj = CropDisease.objects.filter(cropname=name)
    my_dict = {'crop_list': obj,}
    return render(request, "CropDisease/diseases.html" ,context = my_dict)
