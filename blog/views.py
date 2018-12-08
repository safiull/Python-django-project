from django.shortcuts import render
from .models import *

def index(request):

    post = article.objects.all()

    context = {
        "post":post
    }
    print(context)
    return render(request, 'index.html', context)




def getauthor(request, name):
    return render(request, 'profile.html')


def getsingle(request, id):
    post = author.objects.get(pk=id)

    context = {
        'post':post
    }

    return render(request, 'single.html', context)


def getTopic(request, name):
    return render(request, 'category.html')