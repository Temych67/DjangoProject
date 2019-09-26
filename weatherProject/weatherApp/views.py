from django.shortcuts import render
import requests
from .models import City
from .forms import CityForm

def index(request):
	primaryKey='86c3956c863cc7711e40add24b497eee'
	url ='https://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid=' + primaryKey
	
	if(request.method == 'POST'):
		form = CityForm(request.POST)
		form.save()

	form = CityForm()



	cities = City.objects.all()
	all_cities =[]
	
	for city in cities:
		response = requests.get(url.format(city.name)).json()
		city_weather = {
			'city': city.name,
			'temp': response["main"]["temp"],
			'icon': response["weather"][0]["icon"]
		}
		all_cities.append(city_weather)

	context = {'all_info':all_cities,'form':form}

	return render(request,'weather/index.html',context)