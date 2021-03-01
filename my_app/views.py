from django.shortcuts import render
import re
import requests
from requests.compat import quote_plus
from .models import Search
from . import models
from bs4 import BeautifulSoup
from  bs4.element import Tag

# See minute 5:47
'''
page = requests.get(
    'https://forecast.weather.gov/MapClick.php?lat=41.8843&lon=-87.6324#.XIRQYFNKgUE'
)
'''
BASE_CRAIGSLIST_URL = 'https://fresno.craigslist.org/search/?query=web+development'
# Create your views here.

def home(request):
    return render(request, 'base.html')

def new_search(request):

    
    search  = request.POST.get('search')
    # idk if this is safe to do but this line of models saves the search inquiries into database
    models.Search.objects.create(search=search)
    final_url = BASE_CRAIGSLIST_URL.format(quote_plus(search))
    response = requests.get(final_url)
    data = response.text
    print(data)
    soup = BeautifulSoup(data, features='html.parser')


    post_listings = soup.find_all()

    post_titles = post_listings[0].find(class_='product-title-link').text
    post_url = post_listings[0].find('a').get('href')
    post_price = post_listings[0].find(class_="search-result-productprice").text

    final_postings = []

    for post in post_listings:
        post_title = post.find(class_='product-title-link').text
        post_url = post.find('a').get('href')
        post_price = post.find(class_='search-result-productprice').text

    final_postings.append((post_title, post_url, post_price))

    # To send to front-end, same as using context = {'search': search}
    stuff_for_frontend = {
        'search': search,
        'final_postings': final_postings,
        }
        
    return render(request, 'new_search.html')


