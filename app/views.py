from django.shortcuts import render
import json
import requests
from django.http import HttpResponseRedirect
from django.contrib import messages


# Create your views here.

def home(request):
    base_url = 'https://api.openweathermap.org/data/2.5/weather?q={}&appid=2f06e6f5e6e8e6466af3191b662f156b&units=metric'

    try:
        if 'city' in request.POST:
            city = request.POST['city']
        else:
            city = 'indore'

        url = base_url.format(city)
        print(url)

        data = requests.get(url).json()
        # print(data)

        city_name = data['name']
        icon = data['weather'][0]['icon']
        temp = data['main']['temp']
        country = data['sys']['country']
        # print(f'{city_name} {icon} {temp}')

        icon_url = f'https://openweathermap.org/img/wn/{icon}@2x.png'
        # print(icon_url)

        return render(request, 'index.html',context={'city_name':city_name, 'icon':icon, 'temp':temp, 'icon_url':icon_url, 'country':country})
    
    except Exception:
        # print('City not found')
        messages.error(request, 'city not found')
        return HttpResponseRedirect('/')