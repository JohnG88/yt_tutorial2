from django.shortcuts import render
import re
#import requests
#from requests.compat import quote_plus
#from .models import Search
from bs4 import BeautifulSoup
from  bs4.element import Tag

'''
page = requests.get(
    'https://forecast.weather.gov/MapClick.php?lat=41.8843&lon=-87.6324#.XIRQYFNKgUE'
)
'''
# Create your views here.

def home(request):
    return render(request, 'base.html')

def new_search(request):
    search  = request.POST.get('search')

    # To send to front-end, same as using context = {'search': search}
    stuff_for_frontend = {'search': search}
    print(search)

    return render(request, 'new_search.html', stuff_for_frontend)