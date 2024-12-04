from django.shortcuts import render, redirect
from django.views import View
from django.contrib import messages

from weather.forms import CityForm
from weather.weather_api_client import WeatherAPIClient
from weather.models import Favorites, SearchHistory



class GetWeatherDetails(View):
    def get(self, request, *args, **kwargs):
        form = CityForm()
        city_details = None
        
        return render(request, 'weather/city_form.html', {'form': form, 'city_details': city_details})
    
    def post(self, request, *args, **kwargs):
        form = CityForm(request.POST)
        weather_detail = None
        
        print(f"Hello here {weather_detail}")

        if form.is_valid():
            city_name = form.cleaned_data['city_name']
            weather_api_client = WeatherAPIClient(city=city_name)
            weather_detail = weather_api_client.refactor_and_fetch_weather_details()

            if weather_detail is not None:
                print(weather_detail)
                weather_detail["city"] = city_name
            
            SearchHistory.objects.get_or_create(search=city_name, defaults={"user": request.user})

        return render(request, 'weather/city_form.html', {'form': form, 'weather_detail': weather_detail})


class GetSearchHistory(View):
    def get(self, request):
        search_history = SearchHistory.objects.filter(user=request.user)
        return render(request, 'weather/search_history.html', {'search_histories': search_history})


class GetFavorites(View):
    def get(self, request):
        favorites = Favorites.objects.filter(user=request.user)
        return render(request, 'weather/favorites.html', {'favorites': favorites})


class AddToFavorites(View):
    def post(self, request):
        city_name = request.POST.get('city_name')

        if city_name:
            if not Favorites.objects.filter(user=request.user, search=city_name).exists():
                Favorites.objects.create(user=request.user, search=city_name)
                messages.success(request, f"{city_name} has been added to your favorites!")
            else:
                messages.warning(request, f"{city_name} is already in your favorites.")
        else:
            messages.error(request, "No city name provided.")
        
        return redirect('weather_details')
