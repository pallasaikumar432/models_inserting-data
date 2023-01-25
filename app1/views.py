from django.shortcuts import render

# Create your views here.
from app1.models import *

def display_topics(request):
    QST=topic.objects.all()
    d={'topics':QST}
    return render(request,'display_topics.html',d)


def display_webpages(request):
    QSW=webpages.objects.all()
    d={'webpages':QSW}
    return render(request,'display_webpages.html',d)