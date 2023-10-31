from django.shortcuts import render

# Create your views here.
def fertilizer(request):
    return render(request, "fertilizer/fertilizer.html" )

def liquidfertilizer(request):
    return render(request, "fertilizer/liquidfertilizer.html" )

def granular(request):
    return render(request, "fertilizer/granular.html" )

def singleingredientfertilizer(request):
    return render(request, "fertilizer/singleingredientfertilizer.html" )