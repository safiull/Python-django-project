from django.shortcuts import render
from .models import *


def dirmitory(request):    

    return render(request, 'project/dirmitory.html')



def name(request):

    name = Member_dtl.objects.all()

    context = {
        'name':name
    }

    return render(request, 'project/name.html', context)

def details(request, id):
    
    details = Member_dtl.objects.get(id=id)

    context = {
        'details':details
    }
    return render(request, 'project/details.html', context)