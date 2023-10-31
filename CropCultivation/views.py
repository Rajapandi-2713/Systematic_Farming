from django.shortcuts import render,HttpResponse
from .models import CropCultivation

# Create your views here.
def index(request):
    return render(request, 'index.html')

def cultivation(request):
    crop_list = CropCultivation.objects.all()
    my_dict = {'crop_list': crop_list, }
    return render(request, 'CropCultivation/cropcultivation.html', context = my_dict)

def cropdetails(request, cropname):
    mydata = CropCultivation.objects.get(name=cropname)
    print(type(mydata))
    my_dict = {'crop': mydata}
    return render(request, 'CropCultivation/cultivation.html', context = my_dict)
