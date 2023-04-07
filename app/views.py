from django.shortcuts import render

# Create your views here.
from app.models import *
from django.http import HttpResponse
from django.db.models.functions import Length

def industry_table(request):
    LOI=Industry.objects.all()
    d={'Industry':LOI}
    return render(request,'Industry.html',d)



def actor_table(request):
    LOA=Actor.objects.all()
    LOA=Actor.objects.all().order_by('actor_name')#assending order
    LOA=Actor.objects.all().order_by('-actor_name')#descending order
    LOA=Actor.objects.all().order_by('-actor_name')
    LOA=Actor.objects.filter(industry_name='Sandalwood') #specific sandalwood  records
    LOA=Actor.objects.exclude(industry_name='Sandalwood') #except sandalwood  records
    LOA=Actor.objects.exclude(industry_name='Sandalwood') #except sandalwood  records
    LOA=Actor.objects.order_by(Length('actor_name')) #acording to their length in assecending order
    LOA=Actor.objects.order_by(Length('actor_name').desc()) #acording to their length in descending order




    d={'Actor':LOA}
    return render(request,'Actor.html',d)

def actor_dob(request):
    ADOB=Actor_DOB.objects.all()
    
    ADOB=Actor_DOB.objects.filter(date__gt='1983-05-20') #it will give grater then values
    
    ADOB=Actor_DOB.objects.filter(date__gte='1983-05-20') #it will give grater then values
    
    ADOB=Actor_DOB.objects.filter(date__lt='1983-05-20') #it will give grater then values
    
    #ADOB=Actor_DOB.objects.filter(date__lte='1983-05-20') #it will give grater then values
    
    d={"ADOB":ADOB}
    return render(request,'actor_dob.html',d)


def movie_table(request):
    LOM=Movie.objects.all()
    d={'movie':LOM}
    return render(request,'Movie.html',d)











def insert_date(request):
    an=input("enter a actor name:")
    d=input("enter a date:")
    AO=Actor.objects.get_or_create(actor_name=an)[0]
    AO.save()
    AD=Actor_DOB.objects.get_or_create(actor_name=AO,date=d)[0]
    AD.save()
    return HttpResponse('Date object is created')



def insert_IO(request):
    ind=input("Enter a Industry name")
    IO=Industry.objects.get_or_create(industry_name=ind)[0]
    IO.save()
    return HttpResponse("<h1>The industry object is created</h1>")
def insert_AO(request):
    ind=input("Enter a Industry name    :")
    an=input("enter a name of the actor:")
    email=input("Enter the email")
    IO=Industry.objects.get_or_create(industry_name=ind)[0]
    IO.save()
    AO=Actor.objects.get_or_create(industry_name=IO,actor_name=an,email=email)[0]
    AO.save()
    return HttpResponse("<h1>The actor object is created</h1>")

def insert_MO(request):
    an=input("Enter a Actor name    :")
    mn=input("enter a Movie of the actor:")
    url=input("Enter the Url:")
    AO=Actor.objects.get_or_create(actor_name=an)[0]
    AO.save()
    MO=Movie.objects.get_or_create(actor_name=AO,movie_name=mn,url=url)[0]
    MO.save()
    return HttpResponse("<h1>The movie object is created</h1>")