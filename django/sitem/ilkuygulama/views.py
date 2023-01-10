from django.shortcuts import render
from django.http import HttpResponse

#Bu dosya sayfada ne gösterileceğini belirler.

# Create your views here.

def anasayfaView (request):
    return HttpResponse('Merhaba dünya. Süperrr :))) ')


