from django.urls import path

from weather.views import GetWeatherDetails, GetFavorites, GetSearchHistory, AddToFavorites


urlpatterns = [
    path("", GetWeatherDetails.as_view(), name="get_weather_detail"),
    path("favorites/", GetFavorites.as_view(), name="get_favorites"),
    path("search-history/", GetSearchHistory.as_view(), name="get_search_history"),
    path("add-to-favorites/", AddToFavorites.as_view(), name="add_to_favorites"),
]
