from django.shortcuts import render

# Create your views here.
from app.models import *

def industry_table(request):
    LOI=Industry.objects.all()
    d={'Industry':LOI}
    return render(request,'Industry.html',d)



def actor_table(request):
    LOA=Actor.objects.all()
    d={'Actor':LOA}
    return render(request,'Actor.html',d)


def movie_table(request):
    LOM=Movie.objects.all()
    d={'movie':LOM}
    return render(request,'Movie.html',d)
