from django.shortcuts import render

# Create your views here.
def equipment(request):
    return render(request, "equipments/farmingequipments.html" )

def harvester(request):
    return render(request, "equipments/harvester.html" )

def planter(request):
    return render(request, "equipments/planter.html" )

def watersprayer(request):
    return render(request, "equipments/watersprayer.html" )