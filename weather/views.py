from django.shortcuts import render
from django.http import HttpRequest
import requests
from .models import City
from .forms import CityForm

def index(request):
    appid = '4baf1c25bdf35e27bad765630397bf88'
    url = 'https://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid=' + appid

    if(request.method == 'POST'):
        if 'send' in request.POST:
            form = CityForm(request.POST)
            form.save()
        elif 'delete' in request.POST:
            city_name_to_delete = request.POST['delete'][7:]
            City.objects.filter(name=city_name_to_delete).delete()

    form = CityForm()
    
    cities = City.objects.all()
    all_cities = []

    for city in cities:
        try:
            resp = requests.get(url.format(city.name)).json()
            city_info = {
                'city' : city.name,
                'temp' : resp['main']['temp'],
                'icon' : resp['weather'][0]['icon']
            }
            all_cities.append(city_info)
        except Exception as e:
            print(e.with_traceback)
            city.delete()

    context = {
        'all_info' : all_cities,
        'form' : form
    }
    return render(request, 'weather\index.html', context)
