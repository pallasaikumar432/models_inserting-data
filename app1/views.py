from django.shortcuts import render

# Create your views here.
from app1.models import *
from django.db.models.functions import Length

def display_topics(request):
    QST=topic.objects.all()
    QST=topic.objects.filter(topic_name='Cricket')
    
    d={'topics':QST}
    return render(request,'display_topics.html',d)


def display_webpages(request):
    
    QSW=webpages.objects.filter(topic_name='cricket')
    QSW=webpages.objects.all()[:5:]
    QSW=webpages.objects.filter(topic_name='kabaddi').order_by('-name')
    QSW=webpages.objects.all()
    QSW=webpages.objects.all().order_by(Length('name'))
    QSW=webpages.objects.all().order_by(Length('name').desc())
    QSW=webpages.objects.filter(url__startswith='http')
    d={'webpages':QSW}
    return render(request,'display_webpages.html',d)

def display_access(request):
    QSA=access_records.objects.all().order_by('date')

    d={'access':QSA}
    return render(request,'display_access.html',d)