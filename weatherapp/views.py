from django.shortcuts import render

# Create your views here.

import urllib.request
import json
def index(request):
    if request.method == 'POST':
        lat = request.POST['lat']
        lon = request.POST['lon']
        source = urllib.request.urlopen('http://api.openweathermap.org/data/2.5/weather?lat='+ lat +'&lon=' + lon +'&appid=').read()
        list_of_data = json.loads(source)

        data = {
            "country_code": str(list_of_data['sys']['country']),
            "temp": str(list_of_data['main']['temp']) + ' °C',
            "pressure": str(list_of_data['main']['pressure']),
            "humidity": str(list_of_data['main']['humidity']),
            'main': str(list_of_data['weather'][0]['main']),
            'description': str(list_of_data['weather'][0]['description']),
            'icon': list_of_data['weather'][0]['icon'],
            'name': str(list_of_data['name']),
        }
        print(data)
    else:
        data = {}

    return render(request, "main/index.html", data)
