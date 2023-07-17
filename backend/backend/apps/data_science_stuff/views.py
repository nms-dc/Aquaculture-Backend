from django.shortcuts import render
import requests
from bs4 import BeautifulSoup 
from django.http import HttpResponse
from rest_framework.response import Response
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view, permission_classes
from farms.models import Farms
from geopy.geocoders import Nominatim
import pylunar

@csrf_exempt
@api_view(['post'])
def location_finder(request):

    #getting the data from the request as dictionary format
    farm = request.data
    #filtering farm record
    farm_data = Farms.objects.filter(id=farm['farm_id']).values()
    #extracting the city
    print(farm_data[0]['city'])
    # initialize Nominatim API
    geolocator = Nominatim(user_agent="geoapiExercises")


    # Latitude & Longitude input
    Latitude = farm_data[0]['lat']
    Longitude = farm_data[0]['lng']
    print(Latitude)

    location = geolocator.reverse(str(Latitude)+","+str(Longitude))

    address = location.raw['address']

    # traverse the data
    city = address.get('city', '')
    state = address.get('state', '')
    country = address.get('country', '')
    code = address.get('country_code')
    zipcode = address.get('postcode')
    print('City : ', city)
    print('State : ', state)
    print('Country : ', country)
    print('Zip Code : ', zipcode)




    # enter city name
    city = address.get('city', '')

    # create url
    url = "https://www.google.com/search?q="+"weather"+city

    # requests instance
    html = requests.get(url).content

    # getting raw data
    soup = BeautifulSoup(html, 'html.parser')
    #print(soup)

    # get the temperature
    temp = soup.find('div', attrs={'class': 'BNeawe iBp4i AP7Wnd'}).text

    # this contains time and sky description
    string = soup.find('div', attrs={'class': 'BNeawe tAd8D AP7Wnd'}).text

    # format the data
    data = string.split('\n')
    time = data[0]
    sky = data[1]
    # print(temp)
    # print(data,time,sky)
    result = {'city':city,'data':data, 'time':time,'sky':sky, 'temp':temp}
    return Response(result)




@csrf_exempt
@api_view(['post'])
def moon_status(request):
    #getting the data from the request as dictionary format
    farm = request.data
    #filtering farm record
    farm_data = Farms.objects.filter(id=farm['farm_id']).values()
    #extracting the city
    print(farm_data[0]['city'])
    # initialize Nominatim API
    geolocator = Nominatim(user_agent="geoapiExercises")


    # Latitude & Longitude input
    Latitude = str(farm_data[0]['lat'])
    Longitude = str(farm_data[0]['lng'])
    first_l=Latitude[0]+Latitude[1]
    sec_l = Latitude[3]+Latitude[4]
    thr_l = Latitude[3]+Latitude[4]

    first_ln=Longitude[0]+Longitude[1]
    sec_ln = Longitude[3]+Longitude[4]
    thr_ln = Longitude[3]+Longitude[4]
    print(first_l,sec_l,thr_l, first_ln,sec_ln,thr_ln)

    #getting the moon info based on location:

    mi = pylunar.MoonInfo((first_l, sec_l, thr_l), (first_ln, sec_ln, thr_ln))
    data=mi.update((2023, 7, 15))
    print(mi.age())
    print(mi.phase_name())
    return Response({'moon_status_name':mi.phase_name(),'the_age_moon':mi.age()})