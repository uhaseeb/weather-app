import os, requests


class WeatherAPIClient:
    api_key = os.environ.get("WEATHER_API_KEY")
    url = "https://api.openweathermap.org/data/2.5/weather/"

    def __init__(self, city):
        self.city = city
    
    def get_weather_details(self):
        data = None
        params = {"q": self.city, "appid": self.api_key}
        response = requests.get(url=self.url, params=params)
        
        if response.status_code == "200":
            data = response.json()

        return data
    
    def refactor_and_fetch_weather_details(self):
        weather_details = {}
        weather_details_response = self.get_weather_details()

        if weather_details_response is None:
            return weather_details
        
        weather_response = weather_details_response.get("weather", None)

        if weather_response:
            weather_details["weather_status"] = weather_response.get("main", None)
            weather_details["weather_description"] = weather_response.get("description", None)
        
        weather_main = weather_details_response.get("main", None)

        if weather_main:
            weather_details["temperature"] = weather_main.get("temp", None)
            weather_details["feels_like"] = weather_main.get("feels_like", None)
            weather_details["temperature_min"] = weather_main.get("temp_min", None)
            weather_details["temperature_max"] = weather_main.get("temp_max", None)
            weather_details["pressure"] = weather_main.get("pressure", None)
            weather_details["humidity"] = weather_main.get("humidity", None)
            weather_details["sea_level"] = weather_main.get("sea_level", None)
            weather_details["ground_level"] = weather_main.get("ground_level", None)
        
        weather_wind = weather_details_response.get("wind", None)

        if weather_wind:
            weather_details["wind_speed"] = weather_wind.get("speed")
            weather_details["wind_degree"] = weather_wind.get("deg")

        return weather_details
    