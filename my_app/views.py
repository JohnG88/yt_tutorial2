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

