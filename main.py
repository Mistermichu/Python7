# Previous Code Version available: https://github.com/Mistermichu/Python6

import requests
import json
from functions import select_location, get_date

URL = "https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&hourly=rain&daily=rain_sum&timezone=Europe%2FLondon&start_date={searched_date}&end_date={searched_date}"


class WeatherForecaster:
    def __init__(self, latitude, longitude, searched_date, location_name, url) -> None:
        self.latitude = latitude
        self.longitude = longitude
        self.searched_date = searched_date
        self.location_name = location_name
        self.url = url
        self.rain_data = {}

    def request(self):
        api_data = requests.get(self.url.format(
            latitude=self.latitude, longitude=self.longitude, searched_date=self.searched_date))
        if api_data.status_code == 200:
            api_data = json.loads(api_data.text)
        else:
            print("Bład wczytywania danych.")
            return False
        if not api_data:
            pass
        else:
            rain_sum = api_data["daily"].get("rain_sum")[0]
            try:
                rain_sum = float(rain_sum)
                if rain_sum > 0:
                    rain_info = "Będzie padać"
                    print(rain_info)
                    return rain_info
                elif rain_sum == 0:
                    rain_info = "Nie będzie padać"
                    print(rain_info)
                    return rain_info
                else:
                    rain_info = "Nie wiem"
                    print(rain_info)
                    return rain_info
            except ValueError:
                print("Nie wiem")

    def __setitem__(self, date, rain_info):
        self.rain_data[date] = rain_info

    def __getitem__(self, date):
        return self.rain_data[date]

    def __iter__(self):
        return self


# Run App
latitude, longitude, location_name = select_location()
searched_date = get_date()
weather_forecaste = WeatherForecaster(
    latitude, longitude, searched_date, location_name, URL)
try:
    rain_info = weather_forecaste[searched_date]
    print(rain_info)
except KeyError:
    rain_info = weather_forecaste.request()
    weather_forecaste[searched_date] = rain_info
